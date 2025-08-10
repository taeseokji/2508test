import os
from ultralytics import YOLO

# 'yolov8m.pt' 모델을 불러옵니다.
model = YOLO('yolov8m.pt')

# 결과물이 저장될 안전한 경로를 지정합니다.
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_path = os.path.join(desktop_path, 'yolo_output')

print(f"✅ 결과물이 저장될 경로: '{output_path}'")

try:
    # 객체 감지(prediction)를 실행합니다.
    # save=True를 추가하여 결과물을 파일로 저장하도록 지정합니다.
    results = model(r'C:\Users\GC\Desktop\123.jpg', project=output_path, name='predict_m_model', save=True)
    
    print("\n--- 실행 완료 ---")

    # 실행 후 결과 폴더가 실제로 생성되었는지 확인합니다.
    final_output_dir = os.path.join(output_path, 'predict_m_model')
    if os.path.exists(final_output_dir):
        print(f"✅ 성공: 결과 폴더가 '{final_output_dir}'에 생성되었습니다.")
    else:
        print(f"❌ 실패: 결과 폴더가 생성되지 않았습니다.")
        
except Exception as e:
    print(f"\n--- 오류 발생 ---")
    print(f"코드 실행 중 알 수 없는 오류가 발생했습니다: {e}")