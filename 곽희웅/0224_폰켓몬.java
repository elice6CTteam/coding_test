/*

첫 번째로 풀었을 때
import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
        int count = 0;
        int[] arr = new int[nums.length];

        for(int i: nums) {
            if(Arrays.stream(arr).anyMatch(x -> x == i)) {
                continue;
            }
            arr[count] = i;
            count++;
        }

        int phonekemon = 0;
        for(int j: arr) {
            if(j != 0) {
                phonekemon++;
            }
        }

        if(phonekemon > nums.length/2) {
            return nums.length/2;
        }
        return phonekemon;
    }
}

*/

import java.util.Arrays;
class Solution {
    public int solution(int[] nums) {
        // Stream을 사용해서 distinct()로 중복 제거, toArray()로 새 배열로 누적
        int[] arr = Arrays.stream(nums).distinct().toArray();
        // 만약 중복 제거된 배열이 nums.length/2보다 크다면 nums.length/2 반환
        if(arr.length > nums.length/2)
            return nums.length/2;
        return arr.length;
    }
}