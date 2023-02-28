/*
1차풀이
import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        for(int i=0; i<completion.length; i++) {
            for (int j=0; j<participant.length; j++) {
                if(completion[i].equals(participant[j])) {
                    participant[j] = "0";
                    break;
                }
            }
        }
        for (String count: participant) {
            if(!count.equals("0")) {
                answer = count;
                break;
            }
        }
        return answer;
    }
}*/

/*
2차풀이
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        List<String> list = new ArrayList<>(Arrays.asList(participant));
        for(String i: completion) {
            list.remove(i);
        }
        answer = list.get(0);
        return answer;
    }
}*/

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        // ArrayList보다 LinkedList가 삭제 프로세스가 빠르다.
        // 문자열 배열을 LinkedList로 변환
        LinkedList<String> list = new LinkedList<>(Arrays.asList(participant));
        // 배열 정렬
        Arrays.sort(completion);
        // 리스트 정렬
        Collections.sort(list);
        // completion 배열에 있는 선수들을 리스트에서 하나씩 지워나가면 결국 하나만 남는다.
        for(String i: completion) {
            list.remove(i);
        }
        // 리스트에서 인덱스를 기준으로 값을 가져온다.
        answer = list.get(0);
        return answer;
    }
}