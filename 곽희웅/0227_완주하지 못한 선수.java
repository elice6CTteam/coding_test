/*
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
        LinkedList<String> list = new LinkedList<>(Arrays.asList(participant));
        Arrays.sort(completion);
        Collections.sort(list);
        for(String i: completion) {
            list.remove(i);
        }
        answer = list.get(0);
        return answer;
    }
}