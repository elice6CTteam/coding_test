import java.util.HashMap;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        // key:value로 저장하는 HashMap 사용
        HashMap<String, Integer> count = new HashMap<>();
        for(String[] i: clothes) {
            // HashMap과 clothes 배열 비교
            // 만약 옷의 종류가 key에 있다면 +1, 없다면 종류:1을 삽입
            if(count.containsKey(i[1])) {
                count.put(i[1], count.get(i[1])+1);
            }
            else {
                count.put(i[1], 1);
            }
        }

        // .size = HashMap의 크기
        // 만약 옷의 종류가 하나라면, value값 적용
        if(count.size() == 1) {
            return answer = count.get(clothes[0][1]);
        }
        // 여러개라면, 개수마다 +1을 해서 곱해줌
        else {
            for(int i: count.values()) {
                answer *= (i+1);
            }
        }
        // 개수마다 +1을 해서 곱해주면 아무것도 입지 않은 케이스가 포함되기 때문에 -1을 해서 반환
        return answer-1;
    }
}