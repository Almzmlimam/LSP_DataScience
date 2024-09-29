import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = pickle.load(open('porto.sav', 'rb'))

# Title
st.title('Estimasi Harga Mobil Bekas')

# Section for CSV upload
uploaded_file = st.file_uploader("Unggah file CSV", type="csv")

if uploaded_file is not None:
    # Read and display the CSV
    df = pd.read_csv(uploaded_file)
    st.write("Tabel Data dari CSV:")
    st.dataframe(df)

    # Plotting data
    st.write("Visualisasi Data")

    # Visualisasi 1: Histogram Harga dengan histplot
    fig1, ax1 = plt.subplots()
    sns.histplot(df['price'], bins=20, kde=True, color='skyblue', ax=ax1)
    ax1.set_xlabel('Price')
    ax1.set_ylabel('Count')
    ax1.set_title('Distribusi Harga Mobil Bekas')
    st.pyplot(fig1)

    # Visualisasi 2: Barplot Tahun Mobil dengan barplot
    fig2, ax2 = plt.subplots()
    sns.barplot(x='year', y='price', data=df, ax=ax2)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Price')
    ax2.set_title('Harga Rata-Rata Berdasarkan Tahun Mobil')
    st.pyplot(fig2)

    # Visualisasi 3: Histogram Mileage dengan histplot
    fig3, ax3 = plt.subplots()
    sns.histplot(df['mileage'], bins=20, kde=True, color='green', ax=ax3)
    ax3.set_xlabel('Mileage')
    ax3.set_ylabel('Count')
    ax3.set_title('Distribusi Mileage Mobil')
    st.pyplot(fig3)

    # Visualisasi 4: Barplot Engine Size dengan barplot
    fig4, ax4 = plt.subplots()
    sns.barplot(x='engineSize', y='price', data=df, ax=ax4)
    ax4.set_xlabel('Engine Size')
    ax4.set_ylabel('Price')
    ax4.set_title('Harga Rata-Rata Berdasarkan Ukuran Mesin')
    st.pyplot(fig4)

# Input form for prediction
st.header('Input Data untuk Estimasi Harga')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    
    # Pembulatan hasil prediksi
    price_pound = round(predict[0], 2)  # Pembulatan untuk Pound Sterling (2 desimal)
    price_idr = round(predict[0] * 20800, 0)  # Pembulatan untuk Rupiah (tanpa desimal)
    
    st.write(f'Estimasi harga mobil bekas dalam Pound Sterling: £{price_pound}')
    st.write(f'Estimasi harga mobil bekas dalam IDR: Rp{price_idr:,}')  # Penambahan format ribuan untuk IDR