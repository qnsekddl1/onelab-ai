<h1>🤖ONELAB AI</h1>

<h3>🪧AI 프로젝트 소개</h3>

<li>공모전 게시글 추천 시스템</li>

> 회원이 현재 보고 있는 공모전의 게시글의 제목과 내용을 기반으로 다른 공모전 게시글을 추천 해줍니다.

<h2>🪧목차</h2>

<li>화면</li>
<li>데이터 수집(Data Crowling</li>
<li>Cosine_Similarity를 이용한 유사도 분석</li>
<li>Exhibition View 적용/li>
<li>Exhibition DetailView 수정/li>
<li>수정된 화면면</li>
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
3. 위의 작업들로 얻은 데이터들을 CSV파일로 만들어서 DataSET로 만들었습니다.
<details><summary>➡️Crowling 결과 CSV로 저장 코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/ce09e077-63b4-4fa4-a32c-bb1af8ef4fd8" width="550px">
</details>
4. Web Crowling 하는 과정에서 불필요한 특수문자들을 제외하였습니다.
<details><summary>➡️특수문자 제거 코드</summary>
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/e57984aa-f872-4024-9b61-5007aaa5d40d" width="550px">
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
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/58f8d747-6c1f-4204-bcb0-dae5bc05d4e9" width="800px">
      <li>각 공모전 게시글의 제목과 내용을 결합하여 리스트로 만듭니다.</li>
      <li>공모전의 첫 단어를 제외하고 내용의 첫 4개의 단어를 결합니다.</li>
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

<h3>🪧Exhibition DetailView 수정</h3>
<li>위에서 Exhibition View에서 새로 정의한 'get_recommendations'을 통해 ExhibitionDetailView에 전달하고 이를 detail.html에 출력하였습니다.</li>
  <details><summary>➡️코드</summary>
    <li>'get_recommendation' 함수를 호출하여 유사한 공모전을 추천받습니다.</li>
    <li>context에 'exhibitions'로 추천 받은 공모전을 담아서 detail.html로 전달합니다.</li>
    <img src="https://github.com/onelab-server-ai/onelab-ai/assets/156397913/4e371c13-6263-402c-b41a-45e83fae0f25" width="550px">
  </details>
