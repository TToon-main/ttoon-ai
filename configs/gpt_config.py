from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드

API_KEY = os.getenv("GPT_API_KEY")

GPT_MODEL = "gpt-3.5-turbo-1106" 

SYSTEM = "You are a helpful assistant"

USER1 = """
------------------------------------------------------------------------------------------------------------------------------------------------------------
이야기를 만화로 만들거야. 근데 만화를 만드려면 이야기를 4개의 부분으로 나눠야해.
최대한 이야기의 내용이 보존되게 이야기를 뒤에 나올 '나누기' 함수를 사용하여 4개의 부분으로 나눌거야.
한 부분은 'panel', 입력 이야기는 'inputStroy'라고 지칭할게.
------------------------------------------------------------------------------------------------------------------------------------------------------------
panel 항목들의 설명을 위해 panel의 format 예시를 보여줄게.

<Panel 1: Start of the Summer Vacation>
(JaeHoon is drinking coffee with 3 friends and waiting for a flight to Vietnam.)
,(JaeHoon: a 20's boy with black hair)
,(Time: Morning)
,(Background: Cafe in Korea airport),
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

위의 panel의 format 예시 안에 있는 항목들에 대해 설명해줄게.
한 panel에는 총 6개의 항목이 있어.

1번째 항목은 Situation으로, 나눈 패널의 상황에 대한 묘사를 하는 항목이야.
'panel의 format 예시'에서는 (JaeHoon is drinking coffee with 3 friends and waiting for a flight to Vietnam.)가 Situation 항목이야.
여기서, 너가 창작하여 만들어 내는 것이 아니고, inputStory의 내용이 최대한 보존하면서 분위기와 느낌을 추가해서 작성해줘.
또, 대명사나 1인칭 표현의 사용은 최대한 자제하고, situation에 등장하는 인물과 5번 항목인 Characters에 등장하는 인물을 동일해야해.
그리고, inputStory에서의 ‘my’는 주인공이름’s로, ‘I’와 ‘me’는 주인공 이름으로 바꾸어 작성하고, 모든 panel의 situation은 최대 75 의미토큰으로 작성해줘.

2번쨰 항목은 Characteristics로, 주인공에 대한 특징을 설명하는 항목이야.
'panel의 format 예시'에서는 (JaeHoon: a 20's boy with black hair)가 characteristics 항목이야.
입력이야기와 함께 ((주인공이름: 주인공의 나이, 성별, 헤어스타일, 특징을 묘사하는 문장))을 입력할거야.
또, 주인공의 나이가 20살에서 29살사이 혹은 20대라면 주인공에 대한 특징 항목에서 "20's"라는 표현으로 바꿔서 작성해줘.
그리고, situation에 주인공이 등장한다면 situation항목뒤에 ,((주인공이름: 주인공의 나이, 성별, 헤어스타일, 특징을 묘사하는 문장))을 추가한다.
만약 주인공이 등장하지 않는다면 2번 항목은 생략될 수 있어.

3번째 항목은 (Time:)으로, situation의 시간대에 대한 항목이야.
'panel의 format 예시'에서는 (Time: Morning)가 (Time:) 항목이야.
(Time:)항목을 작성할때에는 morning, afternoon, evening, night, dawn과 같이 명확한 시간대를 알 수 있는 표현을 위주로 사용해줘.
이전 panel의 시간대를 생각해서 시간 순서상 위배되지 않아야하니까 주의해줘.

4번째 항목은 (Background:)로, situation의 배경에 대한 항목인 (Background:)이야.
'panel의 format 예시'에서는 (Background: Cafe in Korea airport)가 (Background:) 항목이야.
situation에 등장하는 장소와 Background 항목에 등장하는 장소를 동일하게 작성해줘
inputStory를 기반으로 날씨에 대한 표현을 추가할 수도 있어. 하지만 창작하면 안되고, 최대한 내용이 보존되도록 해줘.

5번째 항목은 (Characters:)로, situation의 등장하는 인물에 대한 항목이야.
'panel의 format 예시'에서는 (Characters: JaeHoon, 3 Korean boy friends) 항목이야.
그리고 situation에 등장하는 인물들의 이름과 Characters항목에 등장하는 이름이 동일하게 작성해줘.

6번째 항목은 Number of Characters로, situation에 등장하는 인물의 수에 대한 항목이야.
'panel의 format 예시'에서는 (4 Characters)가 Number of Characters이야.
'panel의 format 예시'에서 (4 Characters)인 이유는 (Characters: JaeHoon, 3 Korean friends)에서 등장하는 캐릭터가 총 4명이므로 (4 Characters)가 되는거야.
위와 같은 방식으로 등장하는 캐릭터의 수를 5번 항목 Characters에 등장하는 인물의 수와 동일하게 작성해줘.
------------------------------------------------------------------------------------------------------------------------------------------------------------
이제는 가장 중요한 기능인 '나누기' 함수에 대해 설명해줄게.

inputStory를 4개의 panel로 나눌 때 사용되는 함수로, 고려할 사항들이 좀 더 있어.

1. inputStory에 주인공의 가족이 등장할 시, 각 panel의 주인공의 가족 구성원에 대한 설명 항목을 추가하고 주인공의 가족 명칭 앞에 주인공이름’s을 추가해줘.
예시는 (JaeHoon’s family members are her mother, father, and older brother)와 같아.
하지만, panel의 (Characters:)에 주인공만 등장한다면 추가하지 않아야해.

2. 각 panel들의 항목들간에 의미가 중복되는 단어의 사용은 자제해줘.
예시로,
(When JaeHoon was 7 years old, JaeHoon went on a family vacation with his family. They went to the beautiful beach. JaeHoon was lying down couch and drinking orange juice.)
,((JaeHoon: A 7-year-old boy with a black t-shirt and black hair))
,(5 Characters)
,(JaeHoon’s family members are her mother, father, and older brother)
는
(JaeHoon went on a family vacation with his family. They went to the beautiful beach. JaeHoon was lying down couch and drinking orange juice.)
,((JaeHoon: A 7-year-old boy with a black t-shirt and black hair))
,(5 Characters)
,(JaeHoon’s family members are her mother, father, and older brother)
로 수정되어야해

3. 각 panel의 항목들은 ,로 연결되어 있어.
4. 각 panel의 제목과 항목 내용들은 모두 영어로 출력해줘.
5. panel 제목과 situation 사이에는 줄바꿈 1번만 해줘.
6. 각 panel 사이에는 줄바꿈을 2번 해줘.
------------------------------------------------------------------------------------------------------------------------------------------------------------
입력이 주어지면, 위의 고려 사항 및 panel 항목들을 참고하여 정의한 ‘나누기’ 함수를 사용하여 inputStory를 4개의 panel로 나눠줘.
입력은 주인공, inputStory에 등장하는 인물의 정보, inputStory와 ‘나누기’로 구성되어 있어.

'나누기' 함수의 입력 예시와 출력 예시를 알려줄게.

((재훈: 검정 머리, 검정색 티셔츠를 입은 20살 남자), (가족: 엄마, 아빠, 형), (친구들: 한국인 남자 3명))
오늘 아침, 비소리에 눈을 떴다. 일어나서 가족과 아침밥으로 계란햄 토스트와 우유를 먹었다. 그리고 나갈 준비를 하여 12시쯤에 집에서 나왔다.
진짜 오랜만에 여행가는 날이라 아침에 비가 와서 많이 걱정했는데 집에서 나올때 되니까 해가 쨍쨍하고 날씨가 너무 좋았다.
공항까지는 아빠가 차로 데려다 주셔서 아주 편하게 갈 수 있었다. 1시에 인천 공항에서 친구들을 만났다. 짐도 붙이고, 출국 수속을 진행하고 안으로 들어왔다.
비행기 탑승까지 1시간이나 남아서 우리끼리 공항안에 있는 스타벅스에 갔다. 우리는 모두 베트남 여행은 처음이라 준비할 것도 찾아볼 것도 정말 많았다.
그래서 카페에서 우리는 1시간동안 핸드폰으로 리서치만 했다. 베트남으로는 4시간 30분정도 걸리기에 비행기에 탑승하고 나는 바로 잠을 잤다.
베트남에 도착하니 정말 날씨가 더웠다. 우리는 택시를 타고 호텔로 이동하였다. 택시비가 정말 생각보다 너무 싸서 깜짝 놀랐다.
저녁으로는 쌀국수를 먹고, 근처 야시장을 가서 놀았다. 우리는 맥주도 한잔하고 야시장의 분위기를 만끽하였다. 행복한 하루였다.
‘나누기’,

와 같이 주어질 거야

그럼 너의 출력은

<Panel 1: The Beginning of the Trip>
(JaeHoon woke up to rain and had breakfast with JaeHoon's family, eating egg and ham toast with milk.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Morning)
,(Background: House, Raining),
,(Characters: JaeHoon, JaeHoon's Family)
,(4 Characters)
,(JaeHoon’s family members are her mother, father, and older brother)

<Panel 2: Heading to the Airport>
(JaeHoon was worried about the rain, but it turned sunny and perfect by the time he left home. JaeHoon's father drove JaeHoon to the airport.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon, Sunny)
,(Background: Car),
,(Characters: JaeHoon, JaeHoon's father)
,(2 Characters)

<Panel 3: Waiting for the flight>
(JaeHoon met 3 korean friends at Incheon Airport at 1PM. We went Starbucks to drinnk coffee while waiting for the flight.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon)
,(Background: Cafe in Korea Incheon Airport),
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

<Panel 4: Night market in Vietnam>
(In Vietnam, the weather was very hot and humid. For dinner, we had pho, then enjoyed the night market with a beer.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Night)
,(Background: Korea Incheon Airport),
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

가 될거야
------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

ASSISTANT1 = """
네, 이해했습니다. 주어진 기능과 형식을 기반으로 주어진 입력 이야기를 4개의 패널로 나누어 보겠습니다. 입력된 이야기에 대한 내용을 최대한 보존하면서 각 항목을 작성하도록 하겠습니다.

inputStory:

오늘 아침, 비소리에 눈을 떴다. 일어나서 가족과 아침밥으로 계란햄 토스트와 우유를 먹었다. 그리고 나갈 준비를 하여 12시쯤에 집에서 나왔다. 진짜 오랜만에 여행가는 날이라 아침에 비가 와서 많이 걱정했는데 집에서 나올 때 되니까 해가 쨍쨍하고 날씨가 너무 좋았다. 공항까지는 아빠가 차로 데려다 주셔서 아주 편하게 갈 수 있었다. 1시에 인천 공항에서 친구들을 만났다. 짐도 붙이고, 출국 수속을 진행하고 안으로 들어왔다. 비행기 탑승까지 1시간이나 남아서 우리끼리 공항 안에 있는 스타벅스에 갔다. 우리는 모두 베트남 여행은 처음이라 준비할 것도 찾아볼 것도 정말 많았다. 그래서 카페에서 우리는 1시간 동안 핸드폰으로 리서치만 했다. 베트남으로는 4시간 30분 정도 걸리기에 비행기에 탑승하고 나는 바로 잠을 잤다. 베트남에 도착하니 정말 날씨가 더웠다. 우리는 택시를 타고 호텔로 이동하였다. 택시비가 정말 생각보다 너무 싸서 깜짝 놀랐다. 저녁으로는 쌀국수를 먹고, 근처 야시장을 가서 놀았다. 우리는 맥주도 한잔하고 야시장의 분위기를 만끽하였다. 행복한 하루였다.

'나누기':

<Panel 1: The Beginning of the Trip>
(JaeHoon woke up to the sound of rain and had breakfast with JaeHoon's family, eating egg and ham toast with milk, then prepared to leave the house around noon.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Morning)
,(Background: House, Raining)
,(Characters: JaeHoon, JaeHoon's Family)
,(4 Characters)
,(JaeHoon’s family members are his mother, father, and older brother)

<Panel 2: Heading to the Airport>
(JaeHoon was worried about the rain, but it turned sunny and perfect by the time he left home. JaeHoon's father drove JaeHoon to the airport.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon, Sunny)
,(Background: Car)
,(Characters: JaeHoon, JaeHoon's father)
,(2 Characters)

<Panel 3: Waiting for the Flight>
(JaeHoon met 3 Korean friends at Incheon Airport at 1 PM. They checked in their luggage, completed the departure procedures, and went to Starbucks inside the airport to do some research for their trip.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon)
,(Background: Cafe in Korea Incheon Airport)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

<Panel 4: Night Market in Vietnam>
(In Vietnam, the weather was very hot and humid. For dinner, they had pho, then enjoyed the night market with a beer, embracing the lively atmosphere.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Night)
,(Background: Night Market in Vietnam)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

위의 '나누기' 함수를 사용하여 주어진 입력 이야기를 4개의 패널로 나누었습니다. 필요한 정보와 상황이 모두 보존되도록 하였습니다.
"""

USER2 = """
------------------------------------------------------------------------------------------------------------------------------------------------------------
'나누기'의 답변 결과는 4개의 panel만 있으면 되. 설명도, inputStory도 다 필요없어. 오직 4개의 panel만 출력해줘.
------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

ASSISTANT2 = """
<Panel 1: The Beginning of the Trip>
(JaeHoon woke up to the sound of rain and had breakfast with JaeHoon's family, eating egg and ham toast with milk, then prepared to leave the house around noon.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Morning)
,(Background: House, Raining)
,(Characters: JaeHoon, JaeHoon's Family)
,(4 Characters)
,(JaeHoon’s family members are his mother, father, and older brother)

<Panel 2: Heading to the Airport>
(JaeHoon was worried about the rain, but it turned sunny and perfect by the time he left home. JaeHoon's father drove JaeHoon to the airport.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon, Sunny)
,(Background: Car)
,(Characters: JaeHoon, JaeHoon's father)
,(2 Characters)

<Panel 3: Waiting for the Flight>
(JaeHoon met 3 Korean friends at Incheon Airport at 1 PM. They checked in their luggage, completed the departure procedures, and went to Starbucks inside the airport to do some research for their trip.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon)
,(Background: Cafe in Korea Incheon Airport)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

<Panel 4: Night Market in Vietnam>
(In Vietnam, the weather was very hot and humid. For dinner, they had pho, then enjoyed the night market with a beer, embracing the lively atmosphere.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Night)
,(Background: Night Market in Vietnam)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)
"""

USER3 = """
((재훈: 검정 머리, 검정색 티셔츠를 입은 20살 남자), (가족: 엄마, 아빠, 형), (친구들: 한국인 남자 3명))
오늘 아침, 비소리에 눈을 떴다. 일어나서 가족과 아침밥으로 계란햄 토스트와 우유를 먹었다. 그리고 나갈 준비를 하여 12시쯤에 집에서 나왔다.
진짜 오랜만에 여행가는 날이라 아침에 비가 와서 많이 걱정했는데 집에서 나올때 되니까 해가 쨍쨍하고 날씨가 너무 좋았다.
공항까지는 아빠가 차로 데려다 주셔서 아주 편하게 갈 수 있었다. 1시에 인천 공항에서 친구들을 만났다. 짐도 붙이고, 출국 수속을 진행하고 안으로 들어왔다.
비행기 탑승까지 1시간이나 남아서 우리끼리 공항안에 있는 스타벅스에 갔다. 우리는 모두 베트남 여행은 처음이라 준비할 것도 찾아볼 것도 정말 많았다.
그래서 카페에서 우리는 1시간동안 핸드폰으로 리서치만 했다. 베트남으로는 4시간 30분정도 걸리기에 비행기에 탑승하고 나는 바로 잠을 잤다.
베트남에 도착하니 정말 날씨가 더웠다. 우리는 택시를 타고 호텔로 이동하였다. 택시비가 정말 생각보다 너무 싸서 깜짝 놀랐다.
저녁으로는 쌀국수를 먹고, 근처 야시장을 가서 놀았다. 우리는 맥주도 한잔하고 야시장의 분위기를 만끽하였다. 행복한 하루였다.
‘나누기’,
"""

ASSISTANT3 = """
<Panel 1: The Beginning of the Trip>

(JaeHoon woke up to the sound of rain and had breakfast with JaeHoon's family, eating egg and ham toast with milk, then prepared to leave the house around noon.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Morning)
,(Background: House, Raining)
,(Characters: JaeHoon, JaeHoon's Family)
,(4 Characters)
,(JaeHoon’s family members are his mother, father, and older brother)

<Panel 2: Heading to the Airport>

(JaeHoon was worried about the rain, but it turned sunny and perfect by the time he left home. JaeHoon's father drove JaeHoon to the airport.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon, Sunny)
,(Background: Car)
,(Characters: JaeHoon, JaeHoon's father)
,(2 Characters)

<Panel 3: Waiting for the Flight>

(JaeHoon met 3 Korean friends at Incheon Airport at 1PM. They checked in their luggage, completed the departure procedures, and went to Starbucks inside the airport to do some research for their trip.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Afternoon)
,(Background: Cafe in Korea Incheon Airport)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)

<Panel 4: Night Market in Vietnam>

(In Vietnam, the weather was very hot and humid. For dinner, they had pho, then enjoyed the night market with a beer, embracing the lively atmosphere.)
,(JaeHoon: a 20's boy with black hair wearing black t-shirts)
,(Time: Night)
,(Background: Night Market in Vietnam)
,(Characters: JaeHoon, 3 Korean boy friends)
,(4 Characters)
"""