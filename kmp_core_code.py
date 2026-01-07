''' 
 * 暴力匹配算法 (Brute Force)：性能对比的基准
 * 标准 KMP 算法：使用标准的 next 数组
 * 优化 KMP 算法：使用优化的 nextval 数组（解决 AAAAB 这类重复字符回溯效率低的问题）
 * 性能分析工具：自动生成测试数据并计算运行时间
第一部分：核心算法代码
'''
import time
import random
import string

class KMPAlgorithm:
    def __init__(self):
        pass

    # ==========================================
    # 1. 暴力匹配算法 (Brute Force) 
    # ==========================================
    def search_brute_force(self, text, pattern):
        """
        输入: 主串 text, 模式串 pattern
        输出: 匹配的起始索引 (未找到返回 -1)
        """
        n = len(text)
        m = len(pattern)
        
        start_time = time.perf_counter()                  # 开始计时
        
        for i in range(n - m + 1):
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                end_time = time.perf_counter()
                return i, (end_time - start_time) * 1000  # 返回索引和毫秒数
        
        end_time = time.perf_counter()
        return -1, (end_time - start_time) * 1000

    # ==========================================
    # 2. 标准 KMP 算法
    # ==========================================
    def get_next(self, pattern):
        """ 计算标准的 next 数组 """
        m = len(pattern)
        next_arr = [0] * m
        next_arr[0] = -1
        k = -1
        j = 0
        
        while j < m - 1:
            if k == -1 or pattern[j] == pattern[k]:
                j += 1
                k += 1
                next_arr[j] = k
            else:
                k = next_arr[k]
        return next_arr

    def search_kmp_standard(self, text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0: return 0, 0
        
        start_time = time.perf_counter()                  #计算运行时间
        
        next_arr = self.get_next(pattern)
        i = 0 
        j = 0 
        
        while i < n and j < m:
            if j == -1 or text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j] 
        
        end_time = time.perf_counter()                   #计算运行时间
        elapsed = (end_time - start_time) * 1000         #计算运行时间
        
        if j == m:
            return i - j, elapsed
        else:
            return -1, elapsed

    # ==========================================
    # 3. 优化 KMP 算法
    # ==========================================
    def get_next_val(self, pattern):
        """ 计算优化的 nextval 数组 """
        m = len(pattern)
        next_val = [0] * m
        next_val[0] = -1
        k = -1
        j = 0
        
        while j < m - 1:
            if k == -1 or pattern[j] == pattern[k]:
                j += 1
                k += 1
                if pattern[j] != pattern[k]:
                    next_val[j] = k
                else:
                    next_val[j] = next_val[k]
            else:
                k = next_val[k]
        return next_val

    def search_kmp_optimized(self, text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0: return 0, 0
        
        start_time = time.perf_counter()
        
        next_val = self.get_next_val(pattern)
        i = 0 
        j = 0 
        
        while i < n and j < m:
            if j == -1 or text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = next_val[j] 
        
        end_time = time.perf_counter()
        elapsed = (end_time - start_time) * 1000
        
        if j == m:
            return i - j, elapsed
        else:
            return -1, elapsed

# ==========================================
# 4. 性能分析与测试主程序
# ==========================================
if __name__ == "__main__":
    kmp = KMPAlgorithm()

    # --- 场景 A: 常规短字符串测试 ---
    print("--- 场景 A: 功能正确性验证 ---")
    text_demo = "ABABDABACDABABCABAB"
    pattern_demo = "ABABCABAB"
    
    print(f"主串: {text_demo}")
    print(f"模式串: {pattern_demo}")
    
    idx_bf, _ = kmp.search_brute_force(text_demo, pattern_demo)
    idx_std, _ = kmp.search_kmp_standard(text_demo, pattern_demo)
    idx_opt, _ = kmp.search_kmp_optimized(text_demo, pattern_demo)
    
    # 获取 Next 数组供前端展示
    next_arr = kmp.get_next(pattern_demo)
    next_val = kmp.get_next_val(pattern_demo)

    print(f"BF 结果索引: {idx_bf}")
    print(f"Standard KMP 结果索引: {idx_std}")
    print(f"Optimized KMP 结果索引: {idx_opt}")
    print(f"Standard Next 数组: {next_arr}")
    print(f"Optimized NextVal 数组: {next_val}")
    print("\n")

    # --- 场景 B: 性能分析 (KMP 优势场景) ---
    # KMP 在主串包含大量重复字符，且模式串也包含重复字符时优势最大
    print("--- 场景 B: 性能测试 (KMP 优势场景) ---")

    n_size = 100000 
    m_size = 1000    
    
    large_text = "A" * n_size + "B"
    large_pattern = "A" * (m_size - 1) + "B"
    
    print(f"主串长度: {len(large_text)}, 模式串长度: {len(large_pattern)}")
    print("正在计算...")

    idx_bf, time_bf = kmp.search_brute_force(large_text, large_pattern)
    idx_std, time_std = kmp.search_kmp_standard(large_text, large_pattern)
    idx_opt, time_opt = kmp.search_kmp_optimized(large_text, large_pattern)

    #格式化输出
    print(f"{'算法类型':<20} | {'匹配位置':<10} | {'耗时 (ms)':<15}")
    print("-" * 55)
    print(f"{'Brute Force':<20} | {idx_bf:<10} | {time_bf:.4f}")
    print(f"{'Standard KMP':<20} | {idx_std:<10} | {time_std:.4f}")
    print(f"{'Optimized KMP':<20} | {idx_opt:<10} | {time_opt:.4f}")

'''
代码中的输入与输出
 * 输入：
   * text (String): 被搜索的长字符串。
   * pattern (String): 要查找的子串。
 * 输出：
   * index (int): 匹配成功的起始位置。
   * time (float): 算法运行的毫秒数。
   * 给前端的数据：前端画图需要 next 数组和 nextval 数组, 通过 get_next 和 get_next_val 函数单独提供
'''

'''
性能分析的策略
 * 普通随机字符串：KMP 和 暴力法速度差不多，甚至暴力法更快（因为 KMP 有预处理开销）。
 * Worst Case (坏例子)：Text = "AAAA...AB", Pattern = "AAAB"。用这种数据来演示，才能看到时间上的巨大差异（如 1000ms vs 2ms）。
'''