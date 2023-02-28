/*
1차 풀이
import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        int[] arr = Arrays.stream(phone_book).mapToInt(Integer::parseInt).toArray();
        for(int i=0; i<arr.length; i++) {
            for(int j=i+1; j<arr.length; j++) {
                if(String.valueOf(arr[j]).startsWith(String.valueOf(arr[i]))) {
                    answer = false;
                    break;
                }
            }
            if(answer == false) {
                break;
            }
        }
        return answer;
    }
}*/

import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        // 오름차순 정렬
        Arrays.sort(phone_book);
        // 다음 문자열이 전 문자열로 시작된다면 false 반환
        for(int i=1; i<phone_book.length; i++) {
            if(phone_book[i].startsWith(phone_book[i-1])) {
                answer= false;
            }
        }
        return answer;
    }
}
