def read_mat():
    """5x5 행렬 입력받기"""
    mat = []
    for _ in range(5):
        row = list(map(int, input().split()))
        mat.append(row)
    return mat


# 반사 관계 체크
def ref(mat):
    for i in range(5):
        if mat[i][i] != 1:
            return False
    return True


def sym(mat):
    # 대칭 관계인지 확인
    for i in range(5):
        for j in range(5):
            if mat[i][j] == 1 and mat[j][i] != 1:
                return False
    return True


def tri(mat):
    """추이 관계 판별 - 모든 i,j,k에 대해 확인"""
    n = 5
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                for k in range(n):
                    if mat[j][k] == 1 and mat[i][k] != 1:
                        return False
    return True


def cls(x, mat):
    # x의 동치류 구하기
    result = []
    for i in range(5):
        if mat[x-1][i] == 1:  # x는 1-based
            result.append(i+1)
    return set(result)


# 반사 폐포 만들기
def ref_clo(mat):
    new_mat = [row[:] for row in mat]  # deep copy
    for i in range(5):
        new_mat[i][i] = 1
    return new_mat


def sym_clo(mat):
    """대칭 폐포 생성"""
    new_mat = [row[:] for row in mat]
    for i in range(5):
        for j in range(5):
            if new_mat[i][j] == 1:
                new_mat[j][i] = 1
    return new_mat


def trn_clo(mat):
    # Warshall 알고리즘으로 추이 폐포 계산
    result = [row[:] for row in mat]
    
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if result[i][k] and result[k][j]:
                    result[i][j] = 1
    
    return result


def cnt(mat):
    """관계에 포함된 순서쌍 개수 세기"""
    count = 0
    for row in mat:
        count += sum(row)
    return count


def print_mat(mat, title="Matrix:"):
    print(title)
    for row in mat:
        print(' '.join(map(str, row)))
    print()


def check_equiv(mat, show_classes=True):
    """동치 관계 여부 판별 및 출력"""
    is_ref = ref(mat)
    is_sym = sym(mat)
    is_tri = tri(mat)
    
    print(f"Reflexive: {is_ref}")
    print(f"Symmetric: {is_sym}")
    print(f"Transitive: {is_tri}")
    
    is_equiv = is_ref and is_sym and is_tri
    
    if is_equiv:
        print("This relation IS an equivalence relation.\n")
        if show_classes:
            print("Equivalence classes:")
            for x in range(1, 6):
                eq_class = cls(x, mat)
                print(f"  Class of {x}: {eq_class}")
            print()
    else:
        print("This relation is NOT an equivalence relation.\n")
    
    return is_equiv


if __name__ == "__main__":
    print("Enter 5x5 relation matrix (5 lines, each with 5 binary values):")
    original = read_mat()
    
    print("\n" + "="*50)
    print("ORIGINAL RELATION")
    print("="*50)
    print_mat(original, "Input matrix:")
    
    pair_count = cnt(original)
    print(f"Number of pairs in R: {pair_count}\n")
    
    check_equiv(original)
    
    # 반사 폐포
    print("="*50)
    print("REFLEXIVE CLOSURE")
    print("="*50)
    print_mat(original, "Before:")
    ref_closure = ref_clo(original)
    print_mat(ref_closure, "After:")
    check_equiv(ref_closure)
    
    # 대칭 폐포
    print("="*50)
    print("SYMMETRIC CLOSURE")
    print("="*50)
    print_mat(original, "Before:")
    sym_closure = sym_clo(original)
    print_mat(sym_closure, "After:")
    check_equiv(sym_closure)
    
    # 추이 폐포
    print("="*50)
    print("TRANSITIVE CLOSURE")
    print("="*50)
    print_mat(original, "Before:")
    trn_closure = trn_clo(original)
    print_mat(trn_closure, "After:")
    check_equiv(trn_closure)
