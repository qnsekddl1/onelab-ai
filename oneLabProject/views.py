import math
import os
import ssl
from pathlib import Path
from urllib import request

import joblib
import numpy as np
import requests
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from sklearn.metrics.pairwise import cosine_similarity

from community.models import Community
from django.utils import timezone
from exhibition.models import Exhibition
from django.db.models import Q, Sum
from member.models import MemberFile, Member
from member.serializers import MemberSerializer
from onelab.models import OneLab
from place.models import Place
from school.models import School
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import os.path
from pathlib import Path
import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from onelab.models import OneLab
from member.models import Member
from tag.models import Tag


from share.models import Share
from visitRecord.models import VisitRecord

ssl._create_default_https_context = ssl._create_unverified_context

from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response

from django.shortcuts import render
from django.views import View
from django.utils import timezone
from onelab.models import OneLab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from pathlib import Path
import os

# views.py

import math
import os
import ssl
from pathlib import Path
import joblib
import numpy as np
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from onelab.models import OneLab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from visitRecord.models import VisitRecord

ssl._create_default_https_context = ssl._create_unverified_context

# class MainView(View):
#     def get(self, request):
#         member_tag = request.session.get('member', {}).get('tag')
#         if member_tag is None:
#             print('태그 출력 실패')
#             recommended_onelabs = []
#         else:
#             print(f'멤버 태그 출력 = {member_tag}')
#             # AI 서비스를 통해 원랩 추천
#             recommended_onelabs = get_recommendations(member_tag)
#         places = Place.objects.all()
#         place_info = {
#             'places': []
#         }
#         # place 파일쪽
#         for place in places:
#             place_files = list(place.placefile_set.values('path'))
#             place_info['places'].append({
#                 'files': place_files,
#                 'place_title': place.place_title,
#                 'place_address': place.school.school_member_address,
#                 'place_points': place.place_points,
#                 'place_date': place.place_date,
#                 'place_id': place.id,
#                 'school_name': place.school.school_name,
#                 'created_date': place.created_date,
#             })
#         # 공모전쪽
#         exhibitions = Exhibition.objects.all()
#         exhibition_info = {
#             'exhibitions': []
#         }
#         # 공모전 파일쪽
#         for exhibition in exhibitions:
#             exhibition_files = list(exhibition.exhibitionfile_set.values('path'))
#             exhibition_info['exhibitions'].append({
#                 'files': exhibition_files,
#                 'exhibition_title': exhibition.exhibition_title,
#                 'exhibition_content': exhibition.exhibition_content,
#                 'exhibition_status': exhibition.exhibition_status,
#             })
#         # 쉐어쪽
#         shares = Share.objects.all()
#         share_info = {
#             'shares': []
#         }
#         # 쉐어 파일쪽
#         for share in shares:
#             share_files = list(share.sharefile_set.values('path'))
#             share_info['shares'].append({
#                 'files': share_files,
#                 'id': share.id,
#                 'share_title': share.share_title,
#                 'share_content': share.share_content,
#                 'share_points': share.share_points,
#                 'share_choice_major': share.share_choice_grade,
#                 'share_type': share.share_type,
#                 'share_text_major': share.share_text_major,
#                 'share_text_name': share.share_text_name,
#                 'share_choice_grade': share.share_choice_grade,
#             })
#         # 원랩쪽
#         onelabs = OneLab.objects.all()
#         onelab_info = {
#             'onelabs': []
#         }
#         # 원랩 파일쪽
#         for onelab in recommended_onelabs:
#             onelab_files = list(onelab.onelabfile_set.values('path'))
#             onelab_info['onelabs'].append({
#                 'files': onelab_files,
#                 'onelab_main_title': onelab.onelab_main_title,
#                 'onelab_content': onelab.onelab_content,
#             })
#         # 방문자 기록
#         visit_record, created = VisitRecord.objects.get_or_create(date=timezone.now().date())
#         if created:
#             visit_record.count = 1
#         else:
#             visit_record.count += 1
#         visit_record.save()
#         # 멤버쪽
#         member_id = request.session.get('member', {}).get('id')
#         default_profile_url = 'https://static.wadiz.kr/assets/icon/profile-icon-1.png'
#         if member_id is None:
#             profile = default_profile_url
#         else:
#             request.session['member_name'] = MemberSerializer(
#                 Member.objects.get(id=member_id)).data
#             profile = MemberFile.objects.filter(member_id=member_id).first()
#             if profile is not None:
#                 profile = profile.file.url
#             else:
#                 profile = default_profile_url
#         context = {
#             'places': places,
#             'exhibitions': exhibitions,
#             'shares': shares,
#             'onelabs': onelab_info['onelabs'],
#             'profile': profile,
#         }
#         return render(request, 'main/main-page.html', context)




from pathlib import Path
import joblib
import os

from django.shortcuts import render
from django.views import View


from pathlib import Path
import numpy as np
import random
import os


def get_index_from_member_tag(member_tag):
    """
    세션에서 멤버 태그를 가져와 해당 태그에 해당하는 원랩의 인덱스를 반환합니다.
    """
    onelabs = list(OneLab.objects.filter(tag__tag_name=member_tag))  # 세션에서 가져온 멤버 태그를 기반으로 원랩을 가져옵니다.
    if not onelabs:
        return None, None
    onelabs_list = [f"{onelab.onelab_main_title} {onelab.onelab_content} {onelab.onelab_detail_content}" for onelab
                    in onelabs]  # 원랩 정보를 합쳐 리스트로 만듭니다.
    vectorizer = CountVectorizer()  # CountVectorizer를 초기화합니다.
    content_vectors = vectorizer.fit_transform(onelabs_list)  # 원랩 내용을 벡터화합니다.
    similarity_matrix = cosine_similarity(content_vectors)  # 유사도 행렬을 계산합니다.
    mean_similarity_scores = np.mean(similarity_matrix, axis=1)  # 평균 유사도를 계산합니다.
    max_similarity_index = np.argmax(mean_similarity_scores)  # 평균 유사도가 가장 높은 인덱스를 찾습니다.
    return max_similarity_index, content_vectors  # 최대 유사도 인덱스와 벡터를 반환합니다.


def recommend_similar_onelabs(member_tag, content_vectors, num_recommendations=3):
    """
    세션에서 멤버 태그를 기반으로 유사한 원랩을 추천합니다.
    """
    if content_vectors is None:
        return []  # onelab 데이터베이스가 비어 있을 경우 빈 리스트 반환

    max_similarity_index, _ = get_index_from_member_tag(member_tag)  # 세션에서 가져온 멤버 태그에 해당하는 원랩의 인덱스와 벡터를 찾습니다.
    similarity_scores = cosine_similarity(content_vectors[max_similarity_index], content_vectors)  # 해당 원랩과 다른 원랩 간의 유사도를 계산합니다.

    # 유사도가 높은 순으로 정렬된 인덱스 배열
    similar_onelab_indices = similarity_scores.argsort()[0]
    print(f'유사도가 높은 순으로 정렬된 인덱스 배열 {similar_onelab_indices}')

    # 최대 유사도와 동일한 원랩을 제외하고 추천 목록에 추가
    recommended_onelabs = []
    for idx in similar_onelab_indices[::-1]:
        if len(recommended_onelabs) == num_recommendations:
            break
        if idx != max_similarity_index:
            recommended_onelabs.append(OneLab.objects.get(id=idx))

    # ✨ 만약 추천 목록에 포함된 원랩이 num_recommendations 개수보다 적다면, 남은 원랩을 랜덤하게 추가
    remaining_recommendations = num_recommendations - len(recommended_onelabs)
    remaining_onelabs = list(
        OneLab.objects.exclude(id=max_similarity_index).exclude(id__in=[onelab.id for onelab in recommended_onelabs]).order_by('?')[
        :remaining_recommendations])
    recommended_onelabs.extend(remaining_onelabs)

    return recommended_onelabs


def get_member_recommendations(member_id):
    # 회원 정보를 가져온다.
    member = Member.objects.get(id=member_id)

    # 회원의 태그를 가져온다.
    member_tag = member.tag.tag_name if member.tag else None

    # get_index_from_member_tag 함수 호출하여 content_vectors와 max_similarity_index 가져오기
    max_similarity_index, content_vectors = get_index_from_member_tag(member_tag)

    if max_similarity_index is None or content_vectors is None:
        return []  # onelab 데이터베이스가 비어 있을 경우 빈 리스트 반환

    # 회원과 연관된 원랩을 가져온다.
    onelab_tag = OneLab.objects.filter(tag__tag_name=member_tag)

    # 추천 원랩을 가져온다.
    recommended_onelabs = recommend_similar_onelabs(member_tag, content_vectors)  # content_vectors 전달

    # 랜덤하게 추천 원랩을 선택한다.
    random_onelab = random.choice(onelab_tag)

    # 선택된 랜덤 원랩을 결과에 추가한다.
    recommended_onelabs.append(random_onelab)

    return recommended_onelabs



class MainView(View):
    def get(self, request):
        member_id = request.session.get('member', {}).get('id')
        if member_id is None:
            print('회원 ID 없음')
            member_tag = None
            recommended_onelabs = []
        else:
            # 회원의 추천 원랩 가져오기
            recommended_onelabs = get_member_recommendations(member_id)

        # 디버그: 추천된 원랩 목록 출력
        for onelab in recommended_onelabs:
            print(f"추천 원랩: {onelab.onelab_main_title}")

        # 장소 정보 가져오기
        places = Place.objects.all()
        place_info = {
            'places': []
        }
        for place in places:
            place_files = list(place.placefile_set.values('path'))
            place_info['places'].append({
                'files': place_files,
                'place_title': place.place_title,
                'place_address': place.school.school_member_address,
                'place_points': place.place_points,
                'place_date': place.place_date,
                'place_id': place.id,
                'school_name': place.school.school_name,
                'created_date': place.created_date,
            })

        # 전시 정보 가져오기
        exhibitions = Exhibition.objects.all()
        exhibition_info = {
            'exhibitions': []
        }
        for exhibition in exhibitions:
            exhibition_files = list(exhibition.exhibitionfile_set.values('path'))
            exhibition_info['exhibitions'].append({
                'files': exhibition_files,
                'exhibition_title': exhibition.exhibition_title,
                'exhibition_content': exhibition.exhibition_content,
                'exhibition_status': exhibition.exhibition_status,
            })

        # 공유 정보 가져오기
        shares = Share.objects.all()
        share_info = {
            'shares': []
        }
        for share in shares:
            share_files = list(share.sharefile_set.values('path'))
            share_info['shares'].append({
                'files': share_files,
                'id': share.id,
                'share_title': share.share_title,
                'share_content': share.share_content,
                'share_points': share.share_points,
                'share_choice_major': share.share_choice_grade,
                'share_type': share.share_type,
                'share_text_major': share.share_text_major,
                'share_text_name': share.share_text_name,
                'share_choice_grade': share.share_choice_grade,
            })

        # 추천된 원랩 정보 가져오기
        onelab_info = {
            'onelabs': []
        }
        for onelab in recommended_onelabs:
            onelab_files = [file.path for file in onelab.onelabfile_set.all()]
            onelab_info['onelabs'].append({
                'files': onelab_files,
                'onelab_main_title': onelab.onelab_main_title,
                'onelab_content': onelab.onelab_content,
            })

        # 방문 기록 업데이트
        visit_record, created = VisitRecord.objects.get_or_create(date=timezone.now().date())
        if not created:
            visit_record.count += 1
            visit_record.save()

        # 프로필 정보 가져오기
        default_profile_url = 'https://static.wadiz.kr/assets/icon/profile-icon-1.png'
        profile = default_profile_url
        if member_id is not None:
            request.session['member_name'] = MemberSerializer(Member.objects.get(id=member_id)).data
            profile_obj = MemberFile.objects.filter(member_id=member_id).first()
            if profile_obj is not None:
                profile = profile_obj.file.url

        context = {
            'places': places,
            'exhibitions': exhibitions,
            'shares': shares,
            'onelabs': onelab_info['onelabs'],
            'profile': profile,
        }
        return render(request, 'main/main-page.html', context)
def update_member_tag(request, new_tag):
    request.session['member']['tag'] = new_tag
    request.session.modified = True  # 세션 수정 플래그 설정
    member_tag = request.session['member']['tag']
    print(f"세션에 저장된 태그: {request.session['member']['tag']}")  # 디버그 출력


# def get_recommendations(member_tag, num_recommendations=4):
#     # pkl 파일 로드
#     model_path = os.path.join(Path(__file__).resolve().parent, 'test_onelab.pkl')
#     with open(model_path, 'rb') as f:
#         model = joblib.load(f)
#
#     # 모든 원랩 목록을 가져온다.
#     onelabs = list(OneLab.objects.all())  # QuerySet을 리스트로 변환
#
#     # 원랩 내용(제목 + 내용 + 한줄소개)를 수집하여 리스트에 저장
#     onelabs_list = [f"{on.onelab_main_title} {on.onelab_content} {on.onelab_detail_content}" for on in onelabs]

#
#     # CountVectorizer를 사용하여 텍스트 데이터를 벡터화
#     vectorizer = CountVectorizer(lowercase=False)  # lowercase 매개변수를 False로 설정
#     content_vectors = vectorizer.fit_transform(onelabs_list)
#
#     # 회원 태그를 모델에 적용하여 유사도를 계산
#     member_tag_vector = vectorizer.transform([str(member_tag)])  # 문자열로 변환하여 전달
#     similarity_scores = cosine_similarity(member_tag_vector, content_vectors)
#
#     # 유사도가 높은 순으로 원랩 목록 정렬
#     sorted_indices = similarity_scores.argsort()[:, ::-1].flatten()
#
#     # 상위 num_recommendations개의 원랩을 추천
#     recommended_onelabs = [onelabs[i] for i in sorted_indices[:num_recommendations]]
#
#     return recommended_onelabs


# def get_recommendations(member_tag, num_recommendations=4):
#     # pkl 파일 로드
#     model_path = os.path.join(Path(__file__).resolve().parent, 'test_onelab.pkl')
#     with open(model_path, 'rb') as f:
#         model = joblib.load(f)
#         print(f'피클 잘 불러옴: {model}')
#
#     # 모든 원랩 목록을 가져온다.
#     onelabs = list(OneLab.objects.all())  # QuerySet을 리스트로 변환
#
#     # 원랩의 태그를 수집하여 리스트에 저장 (None 값 처리)
#     onelabs_tags = [str(on.tag) if on.tag else "" for on in onelabs]
#
#     # CountVectorizer를 사용하여 태그 데이터를 벡터화
#     vectorizer = CountVectorizer(lowercase=False)  # lowercase 매개변수를 False로 설정
#     content_vectors = vectorizer.fit_transform(onelabs_tags)
#
#     # 회원 태그를 벡터화하여 유사도를 계산 (None 값 처리)
#     member_tag_vector = vectorizer.transform([str(member_tag)]) if member_tag else vectorizer.transform([""])
#     similarity_scores = cosine_similarity(member_tag_vector, content_vectors)
#
#     # 유사도가 높은 순으로 원랩 목록 정렬
#     sorted_indices = similarity_scores.argsort()[:, ::-1].flatten()
#
#     # 유사도 점수를 프린트
#     for idx in sorted_indices[:num_recommendations]:
#         print(f"원랩 제목: {onelabs[idx].onelab_main_title}, 유사도 점수: {similarity_scores[0][idx]}")
#
#     # 상위 num_recommendations개의 원랩을 추천
#     recommended_onelabs = [onelabs[i] for i in sorted_indices[:num_recommendations]]
#
#     # 디버그 출력
#     print(f"추천된 원랩 목록 (태그: {member_tag}): {[onelab.onelab_main_title for onelab in recommended_onelabs]}")
#
#     return recommended_onelabs








