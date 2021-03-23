// 线段树
// 参考链接：https://leetcode-cn.com/problems/range-sum-query-mutable/solution/xian-duan-shu-zu-shou-hui-tu-xiang-yi-qing-er-chu-/

class NumArray {
    int[] tree;
    int n;
    public NumArray(int[] nums) {
        n = nums.length;
        tree = new int[n * 2];
        for(int i = n; i < 2*n; i++){
            tree[i]  = nums[i-n];
        }
        for(int i = n-1; i >= 0; i--){
            tree[i] = tree[i*2] + tree[i*2+1];
        }
    }
    
    public void update(int i, int val) {
        int pos = n + i;
        tree[pos] = val;
        while(pos > 0){
            int left = pos%2==0? pos: pos-1;
            int right = pos%2==0? pos+1: pos;
            tree[pos/2] = tree[left] + tree[right];
            pos /= 2;
        }
    }
    
    public int sumRange(int i, int j) {
        int sum = 0;
        int l = n + i;
        int r = n + j;
        while(r >= l){
            if(l % 2 == 1){
                sum += tree[l];
                l++;
            }
            if(r % 2 == 0){
                sum += tree[r];
                r--;
            }
            l /= 2;
            r /= 2;
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */