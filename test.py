import pandas as pd
from sqlalchemy import create_engine
# 데이터프레임 읽어오기
df = pd.read_csv('NVIDIA_STOCK.csv', header=None)
# PostgreSQL 데이터베이스 연결
engine = create_engine('postgresql://postgres:1234@localhost:5432/stock')
# 테이블 생성 (데이터프레임을 데이터베이스 테이블로 변환)
# df의 첫 번째 행을 컬럼명으로 사용
df.columns = df.iloc[0]
df = df[1:]
# 데이터베이스에 데이터프레임 저장
df.to_sql('nvidia_stock', engine, if_exists='replace', index=False)