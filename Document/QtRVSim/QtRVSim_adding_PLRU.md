# 为QtRVSim添加新特性 - Pseudo LRU 缓存替换策略
## QtRVSim缓存替换策略原版实现
### 父类
```C++
class CachePolicy {
public:
    [[nodiscard]] virtual size_t select_way_to_evict(size_t row) const = 0;

    /**
     * To be called by cache on any change of validity.
     * @param way           associativity way
     * @param row           cache row (index of block/set)
     * @param is_valid      is cache data valid (as in `cd.valid`)
     */
    virtual void update_stats(size_t way, size_t row, bool is_valid) = 0;

    virtual ~CachePolicy() = default;

    static std::unique_ptr<CachePolicy>
    get_policy_instance(const CacheConfig *config);
};
```
- ```select_way_to_evict(size_t row)```
    - 选择被替换的缓存行索引
- ```update_stats(size_t way, size_t row, bool is_valid)```
    - 在每次发生缓存替换时更新内部状态
- ```get_policy_instance(const CacheConfig *config);```
    - 用于获取当前配置下使用的缓存替换策略对象
### LRU/LFU和Random
- LRU即Least Recently Used，在每次需要替换是选取最久没有被用过的缓存行进行替代。从时间局部性的角度来讲，当一个缓存行越久没有被使用，其再次被使用的概率越低。当内存访问模式严格满足时间局部性时，LRU为最优的缓存替换策略。
- LFU为Least Frequently Used，选取被使用频率最小的缓存行进行替代。当内存访问模式中有部分地址会被长期频繁访问时，此种缓存替换策略能保证此类地址不会被从缓存中驱逐。
- Random即为随机选取被替换的缓存行。
以下以Random为例介绍QtRVSim中缓存替换策略的实现：
```C++
CachePolicyRAND::CachePolicyRAND(size_t associativity)
    : associativity(associativity) {
    // Reset random generator to make result reproducible.
    // Random is by default seeded by 1 (by cpp standard), so this makes it
    // consistent across multiple runs.
    // NOTE: Reproducibility applies only on the same execution environment.
    std::srand(1); // NOLINT(cert-msc51-cpp)
}

void CachePolicyRAND::update_stats(size_t way, size_t row, bool is_valid) {
    UNUSED(way) UNUSED(row) UNUSED(is_valid)
    // NOP
}

size_t CachePolicyRAND::select_way_to_evict(size_t row) const {
    UNUSED(row)
    return std::rand() % associativity; // NOLINT(cert-msc50-cpp)
}
```
- ```CachePolicyRAND::CachePolicyRAND(size_t associativity)```
    - 构造函数，Random没有内部状态，只需要对随机数生成进行初始化
- ```CachePolicyRAND::update_stats(size_t way, size_t row, bool is_valid)```
    - 内部状态更新，Random没有内部状态，无需更新
- ```CachePolicyRAND::select_way_to_evict(size_t row)```
    - 随机选取
## Pseudo LRU
### Pseudo LRU原理
- Pseudo LRU或Tree-PLRU是一种高效的算法，用于在给定一组项目和项目的访问事件序列的情况下，选择最有可能最近没有被访问过的项目。理论上讲LRU，即选择最少被使用的缓存行进行驱逐是在最为合理的。但其硬件实现开销过大（尤其是在associativity较大的情况下），因此在硬件中常使用Pseudo LRU进行近似。
- 这种技术用于英特尔486 CPU缓存以及PowerPC家族中许多处理器，例如苹果计算机使用的飞思卡尔的PowerPC G4。
- 该算法的工作原理如下：假设有一个二叉搜索树。树的每个节点都有一个一位标志，表示“向左移动以插入Psedo LRU元素”或“向右移动以插入Pseudo LRU元素”。要找到一个Pseudo LRU元素，根据标志的值遍历树。要使用一个项目N更新树，遍历树以找到N，并在遍历过程中将节点标志设置为指示相反方向的方向。
### Pseudo LRU的QtRVSim实现
```C++
CachePolicyPLRU::CachePolicyPLRU(size_t associativity, size_t set_count)
    : associativity(associativity), associativityCLog2(std::ceil(log2((float)associativity))) {
    plru_ptr.resize(set_count);
    for (auto &row : plru_ptr) {
        row.resize((2 << associativityCLog2)-1,0); // Initially point to block 0
    }
}

void CachePolicyPLRU::update_stats(size_t way, size_t row, bool is_valid) {
    cout<<"Update stats: way="<<way<<" row="<<row<<endl;
    uint32_t plru_idx = 0;
    auto &row_ptr = plru_ptr.at(row);
    if(is_valid) {
        for (uint32_t i = 0; i < associativityCLog2; i++) {
            row_ptr[plru_idx] = ((way >> (associativityCLog2 - 1 - i)) & 1) ? 0 : 1;
            cout<<"plru_idx="<<plru_idx<<" local_ptr="<<((way >> (associativityCLog2 - 1 - i)) & 1)<<endl;
            plru_idx = (1 << (i + 1)) - 1;
            plru_idx += way >> (associativityCLog2 - 1 - i);
        }
    }
}

size_t CachePolicyPLRU::select_way_to_evict(size_t row) const {
    uint32_t idx = 0;
    uint32_t plru_idx = 0;
    auto &row_ptr = plru_ptr.at(row);
    for (uint32_t i = 0; i < associativityCLog2; i++) {
        idx         <<= 1;
        uint32_t ptr  = row_ptr[plru_idx];
        idx          += ptr;
        plru_idx      = (1 << (i + 1)) - 1;
        plru_idx     += idx;
    }
    return (idx >= associativity) ? (associativity - 1) : idx;
}
```
- 独立测试结果
```
Update stats: way=0 row=0
plru_idx=0 local_ptr=0
plru_idx=1 local_ptr=0
plru_idx=3 local_ptr=0
Selected way to evict:4

Update stats: way=1 row=0
plru_idx=0 local_ptr=0
plru_idx=1 local_ptr=0
plru_idx=3 local_ptr=1
Selected way to evict:4

Update stats: way=2 row=0
plru_idx=0 local_ptr=0
plru_idx=1 local_ptr=1
plru_idx=4 local_ptr=0
Selected way to evict:4

Update stats: way=3 row=0
plru_idx=0 local_ptr=0
plru_idx=1 local_ptr=1
plru_idx=4 local_ptr=1
Selected way to evict:4

Update stats: way=4 row=0
plru_idx=0 local_ptr=1
plru_idx=2 local_ptr=0
plru_idx=5 local_ptr=0
Selected way to evict:0

Update stats: way=5 row=0
plru_idx=0 local_ptr=1
plru_idx=2 local_ptr=0
plru_idx=5 local_ptr=1
Selected way to evict:0
```