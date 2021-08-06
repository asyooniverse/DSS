# 기능: 기본 관리
# 함수: index, detail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
# ---------------------------------- [edit] ---------------------------------- #
from django.db.models import Q
# ---------------------------------------------------------------------------- #

from ..models import Question

def index(request):
    """
    pybo 목록출력
    """
    # ---------------------------------- [edit] ---------------------------------- #
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    # ---------------------------------------------------------------------------- #
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # ---------------------------------- [edit] ---------------------------------- #
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    # ---------------------------------------------------------------------------- #
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)