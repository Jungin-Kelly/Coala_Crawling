from urllib.request import urlretrieve #urllib -> 기본 라이브러리임
import ssl                                                            #line2,3은 사이트에서 접근 오류나는 걸 막음
ssl._create_default_https_context =ssl._create_unverified_context

scr = "https://movie-phinf.pstatic.net/20191030_118/1572411669676j0Arb_JPEG/movie_image.jpg?type=m203_290_2"
urlretrieve(scr, "poster.png")