#include <vector>
#include <iostream>
#include <set>
using namespace std;

int solution(vector<int> nums)
{

    int answer = 0;
    int N = nums.size() / 2; 
    set<int> s;
    for (int i = 0; i < nums.size(); i++)
    {
        s.insert(nums[i]);
    }
    if (s.size() <= N)
    {
        answer = s.size();
    }
    else
    {
        answer = N;
    }
    return answer;
}



// line 9 : N 마리중 N/2 설정
/*
line 11 :  container set을 사용하여 중복되는 값을 제거
int array[6] = [1,1,2,2,3,3]
set<int> array; // [1,2,3]
*/
// line 12 ~ 15 : s 배열에 nums의 값들을 차례대로 대입

/*
line 16 ~23 : 중복되는 값을 제거한 s의 배열 크기가 
최대 경우의 수 N 이하인 경우, s의 배열 크기가 answer이고
N보다 큰 경우 N 답은 answer이 된다. 
(경우의 수가 N 보다 클 수 없기때문에)
*/
