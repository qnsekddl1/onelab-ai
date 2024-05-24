<h1>🤖ONELAB AI</h1>

<h3>🪧AI 프로젝트 소개</h3>

<li>공모전 게시글 추천 시스템</li>
회원이 현재 보고 있는 공모전의 게시글의 제목과 내용을 기반으로 다른 공모전 게시글을 추천 해줍니다.

<h2>🪧목차</h2>

<li>화면</li>
<li>데이터 수집(Data Crowling</li>
<li>Cosine_Similarity를 이용한 유사도 분석</li>
<li>Exhibition View 적용/li>
<li>Exhibition DetailView 수정/li>
<li>detail.html 회면 출력 확인</li>
<li>Trouble Shooting</li>
<li>느낀 점</li>

<h3>🪧화면</h3>
<details><summary>➡️AI 적용할 화면</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/1adb14b2-f99b-4a83-aab5-6bfee47e4b79" width="550px">
  <br>
<li>현재는 해당 게시글의 내용과 첨부한 이미지 파일들을 보여주고 있습니다.</li>
</details>

<details><summary>➡️AI 적용 후 예상 화면</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/124604cb-f551-4ad7-badf-bb0ed7359e07" width="550px">
  <br>
<li>회원이 현재 보고 있는 공모전 게시글의 제목과 내용을 기반으로 다른 공모전 게시글과의 유사도를 분석하여 하단에 목록을 나타냅니다.</li>
</details>

***

<h3>🪧데이터 수집(Data Crowling)</h3>
1. 필요로한 공모전의 데이터들은 다른 공모전 모음 사이트를 참고하였습니다.
<details><summary>➡️Web Crowling 사이트</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/090f2663-948c-425c-b884-67ab771031d8" width="550px">
</details>
2. Pycharm에서 BeautifulSoup을 이용하여 Web Crowling을 하여 데이터를 수집하였습니다.
<details><summary>➡️Crowling 코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/cda1b2d7-f2c3-4b48-907d-1d0af81c7115" width="550px">
</details>
3. Web Crowling 하는 과정에서 불필요한 특수문자들을 제외하였습니다.
<details><summary>➡️특수문자 제거 코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/e57984aa-f872-4024-9b61-5007aaa5d40d" width="550px">
</details>
4. 위의 작업들로 얻은 데이터들을 CSV파일로 만들어서 DataSET로 만들었습니다.
<details><summary>➡️Crowling 결과 CSV로 저장 코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/ce09e077-63b4-4fa4-a32c-bb1af8ef4fd8" width="550px">
</details>


***

<h3>🪧Cosine_Similarity 이용하여 유사도 분석</h3>
1. Pycharm에서 생성한 CSV를 Jupyter NoteBook에서 제목과 내용을 이용하여 유사도 분석을 시험 진행 했습니다.
<details><summary>➡️코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/b24044be-92e6-4502-a680-d14f9f1d36e2" width="550px">
</details>
2. 제목과 전체 내용을 하나의 긴 문자열로 합쳐 주었습니다.
<details><summary>➡️코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/a1cc9b62-1b69-4a26-9122-0233ef60cca8="550px">
</details>
3. 합쳐준 문자열을 통해 입력한 키워드(문자열)와의 유사도를 분석하여 제일 높은 5개(제일 유사도가 높은 것은 입력한 키워드이기 때문에 제외)를 출력하였습니다.
<details><summary>➡️코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/5346eece-047c-425f-93f1-5ed9bd7335b1" width="550px">
</details>
4. 입력한 키워드와 결과 출력을 확인 했습니다.
<details><summary>➡️코드</summary>
<li>입력 키워드</li> 
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/f147ba9f-273d-4e70-aed1-0bea176ff447" width="550px">
<li>출력된 결과</li>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/e2ce8373-53c0-4b12-bbdf-1d474ca5ef16" width="550px">
<li>출력된 결과들의 유사도 점수</li>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/351301d6-54b6-4844-a179-a8bceb03b2f2" width="550px">
</details>

***

<h3>🪧Exhibition View 적용</h3>
<li>Jupyter NoteBook에서 테스트 했던 코드들을 Pycharm으로 가져와서 약간 더 수정을 하였습니다.</li>
<details><summary>➡️적용 코드</summary>
  1. 함수 정의 및 모든 데이터 가져오기
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/c8a37e0f-d313-4977-8b56-81182dfa3a4a" width="800px">
      <li>'get_recommendations' 이라는 함수를 정의하였습니다.</li>
      <li>num_recommendations: 추천할 공모전의 수입니다. 기본값은 4입니다.</li>
      <li>'Exhibition' 모델에서 모든 공모전 데이터를 가져옵니다.</li>
    </details>
  2. 공모전 제목과 내용을 결합하여 수집
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/9f1e0e83-8372-4d8c-adf3-ad2a4503f211" width="800px">
      <li>각 공모전 게시글의 제목과 내용을 부분 결합하여 리스트로 만듭니다.</li>
      <li>공모전 제목의 첫 단어를 제외하고 공모전 내용의 2번째 부터 9번째의 단어 결합니다.</li>
    </details>
  3. 텍스트 데이터 백터
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/6985c9cc-4558-4170-8542-ce81d33016de" width="800px">
      <li>'CountVectorizer'를 사용해 전시회 제목과 내용을 벡터화한 다음 'content_vectors'에 저장하였습니다.</li>
    </details>
  4. 코사인 유사도 계산
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/a5c98613-a345-4e8d-b59c-6b8b6ae57f09" width="800px">
      <li>벡터화된 공모전 데이터 간의 코사인 유사도를 계산합니다.</li>
    </details>
  5. 유사도 점수를 기준으로 정렬
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/52252f05-bfd8-470c-8a16-c3b60296b15c" width="800px">
      <li>해당 공모전과 다른 공모전 간의 유사도를 나열합니다.</li>
      <li>유사도 점수를 기준으로 내림차순 정렬합니다.</li>
    </details>
  6. 유사한 공모전 선택
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/dc5040bc-d61c-480f-abd0-9f0f64afbb61" width="800px">
      <li>제일 높은 유사도는 회원이 보고 있는 게시물이기 때문에 제외하고 4개의 유사한 공모전을 선택합니다.</li>
      <li>유사한 공모전의 인덱스를 통해 실제 공모전 데이터를 가져옵니다.</li>
    </details>
  7. 유사한 공모전 반환
    <details><summary>➡️코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/37552a84-e53a-4b5c-88a8-681b0e0cd270" width="400px">
      <li>유사한 공모전 리스트를 반환합니다.</li>
    </details>
</details>

***

<h3>🪧Exhibition DetailView 수정</h3>
<li>위에서 Exhibition View에서 새로 정의한 'get_recommendations'을 통해 ExhibitionDetailView에 전달하고 이를 detail.html에 출력하였습니다.</li>
  <details><summary>➡️코드</summary>
    <li>'get_recommendation' 함수를 호출하여 유사한 공모전을 추천받습니다.</li>
    <li>context에 'exhibitions'로 추천 받은 공모전을 담아서 detail.html로 전달합니다.</li>
    <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/4e371c13-6263-402c-b41a-45e83fae0f25" width="550px">
  </details>

***

<h3>🪧detail.html 회면 출력 확인</h3>
<li>ExhibitionDeatilView에서 context에 담은 exhibitions를 detail.html을 통해 화면에 출력하였습니다.</li>
  <details><summary>➡️화면 확인</summary>
    <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/235b8bbc-7a0e-4d6d-b3a5-cc1f46015cc6" width="550px">
    <li>당초에 계획했던 위치에 'AI가 추천하는 공모전' 이라는 제목으로 추천 게시글 4개가 표시 되는 것을 확인하였습니다.</li>
  </details>

***

<h3>🪧Trouble Shooting</h3>
<li>이번 프로젝트를 진행 하면서 생겼던 문제점 중 가장 큰 문제점은 유사도의 점수가 낮게 나온다는 것이었습니다.</li>
<li>유사도 점수가 0.2 ~ 0.3 정도 밖에 안나왔기 때문에 이 점수를 더 높일 수 있는 방법을 찾아야 했습니다.</li>
<li>몇가지 방법을 생각 하던 도중 공모전의 제목과 내용의 시작 대부분 동일하게 시작한다는 것을 발견 했습니다.</li>
<li><strong>그래서 제목과 내용을 결합 하는 방법을 바꾸어보기로 했습니다.</strong></li><br>
<li>기본적인 방법은 제목 전체와 내용 전체를 하나의 긴 문자열로 결합 하였을 때는 내용이 너무 길어서 유사성을 잘 찾지 못하는 것 같았습니다.</li>
<details><summary>➡️전체 결합 코드, 유사도 점수</summary>
  <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/f64c34d9-3780-4f00-baea-a3508bf2d0e1" width="550px">
  <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/f6c91fc1-61ef-4111-b5d2-be7223783b50" width="550px">
  <li>공모전의 전체 제목과 내용을 결합 하였을 때의 코드와 유사도 점수입니다.</li>
  <li>유사도 점수가 0.41에서 0.45정도로 0.5점을 넘지 못하고 있습니다.</li>
</details>
<li>수정한 결합 방법은 제목의 1번째 단어를 제외한 모든 단어들과 내용의 2번째 단어부터 9번째 단어까지만 결합하여 유사성을 잘 찾을 수 있도록 하는 것이었습니다.</li> 
<details><summary>➡️부분 결합 코드, 유사도 점수</summary>
  <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/06f2c8b7-5682-4cf0-b322-a2f90118dd72" width="550px">
  <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/032c1c00-41d8-420a-9601-976d1419ccf8" width="550px">
  <li>공모전의 제목에서 첫번째 단어를 제외한 나머지 전체와 내용에서 2번째 단어부터 9번째 단어까지만 결합하였습니다.</li>
  <li>유사도 점수가 약 0.72로 0.27 정도 상승하였습니다.</li>
</details>

<li>위의 방법을 통해서 유사도 점수를 높일 수 있었습니다</li>

***

<h3>🏆느낀점</h3>
<li>이번 프로젝트를 통해 Django와 Machine Learning을 결합 할 수 있는 경험과 지식을 얻을 수 있었습니다.</li>
<li>Web Crowling 이라는 기술로 원하는 데이터 수집의 방법을 알 수 있었습니다.</li>
<li>Cosine Similarity를 통해서 유사도 분석을 할 수 있었고 더 나아가 이것을 Django에 사용함으로서 사용자에게 맞는 내용을 추천할 수 있는 기능을 구현할 수 있었습니다.</li>
<li>그리고 Trouble Shooting을 통해, 문제를 좀 더 다각도로 볼수 있었고 그로 이해 문제 해결 능력이 크게 향상이 되었습니다.</li>

***

<h3>🔍개선 사항</h3>

* 추천 시스템 성능 향상
  - 데이터의 부족
    + 현재 저장 되어있는 데이터는 feature가 제목과 내용으로 2개 밖에 없고 총 개수는 1000개 정도로 적은 편입니다.
    + 데이터의 feature가 더 다양해지고, 개수가 더 늘어난다면, 사용자에게 더 정확한 추천이 가능해질듯 합니다.

* 모델 개선
  - 다양한 기술 도입
     + Word Embeddings과 같은 단어 임베팅 기법을 사용하여 단어 간의 의미적 유사성을 반영할 수 있게 되면 유사도를 높일 수 있습니다.
     + 나아가 높아진 유사도를 기반으로 더 정확한 추천을 할 수 있을듯 합니다.
