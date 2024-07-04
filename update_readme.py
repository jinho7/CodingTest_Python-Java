import os

def count_subpackages(directory):
    return len([name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))])

def update_readme():
    # README 템플릿 읽기
    with open('README_template.md', 'r', encoding='utf-8') as file:
        readme_content = file.read()

    # 패키지 수 계산
    subpackage_count = count_subpackages('프로그래머스/1')

    # README 내용 업데이트
    updated_content = readme_content.replace('X', str(subpackage_count))

    # 업데이트된 README 저장
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()
