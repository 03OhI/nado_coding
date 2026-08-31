"""공통 예제 데이터 / 한글 폰트 설정"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def use_korean_font():
    """윈도우 기준 한글 폰트 설정 (깨짐 방지)"""
    matplotlib.rcParams["font.family"] = "Malgun Gothic"
    matplotlib.rcParams["axes.unicode_minus"] = False


def load_scores():
    """학생별 성적 데이터프레임"""
    return pd.DataFrame({
        "이름":   ["이지은", "유재석", "조세호", "박명수", "정준하"],
        "학교":   ["나도고", "나도고", "코딩고", "코딩고", "나도고"],
        "학년":   [1, 2, 3, 1, 2],
        "국어":   [90, 75, 88, 60, 95],
        "영어":   [85, 92, 70, 78, 88],
        "수학":   [78, 88, 95, 65, 91],
    })
