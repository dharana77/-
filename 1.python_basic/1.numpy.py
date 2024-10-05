

# 1 /1만시간
import numpy as np

A = np.array([2,4], [5,-6])

print(f'A = \n{A}|n')

# np.array -> 배열을 만들고 싶으면 np.array에 배열을 넣어준다.


#
# a라는 포인트와 b라는 포인트
#
# 특정한 회전을 적용해주면 b라는 포인트 가 됨
#
# R이라는 회전 행렬을 곱해주면
#
# 회전행렬은
#
# [cos, -sin
# Sin, cos]
#
#
# 이것은 파이썬으로 만들면


def rot_mat(theta):
	return np.arrray([
		[np.cos(theta), -np.sin(theta)],
		[np.sin(theta), np.cose(theta)],
	])


# 이번에는 행렬 곱에 대해

def trans_vec(x, y):
	return


# B = np.array([2], [2])
# D = A.dot(B)
# 인데 연속하려면 계속 써줘야하므로
# 일반적으로
# D_ = A @ B
# 와 같은 방식으로 사용함
#
# A.dot(B)
# 와 A @ B 결과가 같은 것을 실행하면 확인 가능


# transpose를 구현하고 싶다면
A_T = A.transpose()

# 역행렬을 구하고 싶다면
np.linalg.inv(A)

# 주의할점은 모든 행렬이 역행렬이 존재하지 않음
# 존재하지 않은 역행렬을 구하면 오류 예외 처리 반환
#
#
# 행렬 곱셈과  element-wise mult는 다름
#
# inv_a * A
# Np.matmul(inv_a, A)
# inv_a.dot(A)
# Inv_a @ A
#
#
# *기호는 행렬 곱이 아니라 단위끼리 곱하는 것을 의미

theta = 30 * np.pi / 180
# 라디안으로 변경해줘야 하기 때문에

# identity matrix와
# np.zeros
# identity matrix는 하나만 넣어도 행과 열이 같은 행렬 만들거줌

np.zeros((2,4))
# 는 행과 열이 0인 행렬을 만들어줌


