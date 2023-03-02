import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 파이썬의 딕셔너리 역할을 하는 HashMap 사용
        HashMap<String, Integer> list = new HashMap<>();
        // 1번 수행, 장르의 총 재생 수를 더함
        for(int i=0; i<genres.length; i++) {
            if(list.containsKey(genres[i])) {
                list.put(genres[i], list.get(genres[i]) + plays[i]);
            }
            else {
                list.put(genres[i], plays[i]);
            }
        }
        // 총 재생 수를 더한 HashMap list에서 value만 꺼내서 List listValues 선언
        List<Integer> listValues = new ArrayList<>(list.values());
        // List sortedList1을 선언하고 listValues를 내림차순 정렬
        List<String> sortedList1 = new ArrayList<>();
        Collections.sort(listValues, Collections.reverseOrder());

        // listValues를 돌며 sortedList1에 장르 내림차순으로 저장
        for(int j : listValues) {
            // Map.Entry는 Map 형태의 인터페이스를 만드는 데 사용함, For 문에서 돌릴 때나 스트림에서 사용
            // ["classic", "pop"]
            for(Map.Entry<String, Integer> entry: list.entrySet()) {
                if(entry.getValue().equals(j)) {
                    sortedList1.add(entry.getKey());
                }
            }
        }
        // answer 배열의 인덱스 선언
        int count = 0;
        // answer 배열의 크기를 sortedList1의 크기 * 2로 설정
        int[] answer = new int[sortedList1.size() * 2];

        // sortedList1을 돌며 HashMap play에 genres의 인덱스, plays 재생 수를 저장
        // {1=600, 4=2500}
        for(String i: sortedList1) {
            HashMap<Integer, Integer> play = new HashMap<>();
            for(int k=0; k<genres.length; k++) {
                if(genres[k].equals(i)) {
                    play.put(k, plays[k]);
                }
            }

            // 위와 똑같이 List playValues에 play에서 value를 꺼내서 저장
            List<Integer> playValues = new ArrayList<>(play.values());
            // List sortedList2를 선언하고, playValues를 내림차순 정렬
            List<Integer> sortedList2 = new ArrayList<>();
            Collections.sort(playValues, Collections.reverseOrder());

            // playValues를 돌며 재생 수가 큰 항목부터 sortedList2에 저장
            for(int m : playValues) {
                for(Map.Entry<Integer, Integer> entry: play.entrySet()) {
                    if(entry.getValue() == m) {
                        sortedList2.add(entry.getKey());
                    }
                }
            }

            // 만약 크기가 1이라면 하나 저장 후 count + 1
            if(playValues.size() == 1) {
                answer[count] = sortedList2.get(0);
                count++;
            }

            // 만약 2 이상이라면 순차적으로 두 개 저장
            else {
                for(int l=0; l<2; l++) {
                    answer[count] = sortedList2.get(l);
                    count++;
                }
            }
        }

        // 만약 count보다 처음에 설정한 answer 배열의 크기가 더 크다면 count-1 인덱스까지 복사해서 저장
        if(answer.length > count) {
            answer = Arrays.copyOfRange(answer, 0, count);
        }

        return answer;
    }
}