# HalluGuard: Anti-Hallucination Extension for Chatbots

![HalluGuard Logo](https://github.com/aidandf29/HalluGuard/blob/main/HalluGuard.jpg) 

## 📝 Deskripsi Proyek

**HalluGuard** adalah sebuah ekstensi anti-halusinasi untuk chatbot yang dirancang untuk meningkatkan keandalan dan akurasi respons chatbot. Halusinasi dalam chatbot terjadi ketika model menghasilkan respons yang tidak akurat atau tidak relevan. HalluGuard menggunakan model **TinyLlama-1.1B** untuk klasifikasi dan pengecekan fakta, serta mengintegrasikan **Brave Search API** dan **GPT API** sebagai fallback untuk verifikasi fakta.

Proyek ini dikembangkan dengan menggunakan **Streamlit** untuk antarmuka pengguna dan **Node.js** untuk backend. HalluGuard bertujuan untuk memastikan integritas respons chatbot dengan memverifikasi fakta dan membedakan antara fakta dan opini.

## 🚀 Fitur Utama

- **Klasifikasi Fakta dan Opini**: Menggunakan model TinyLlama-1.1B untuk membedakan antara fakta dan opini dalam respons chatbot.
- **Pengecekan Fakta**: Memverifikasi kebenaran fakta menggunakan Brave Search API dan GPT API sebagai fallback.
- **Antarmuka Pengguna yang Ramah**: Dibangun dengan Streamlit, memungkinkan pengguna untuk berinteraksi dengan chatbot dan memverifikasi fakta dengan mudah.
- **Integrasi dengan Database**: Menggunakan PostgreSQL yang dihosting di Supabase untuk menyimpan data pengguna dan riwayat chat.

## 🛠️ Teknologi yang Digunakan

- **Frontend**: Streamlit (Python)
- **Backend**: Node.js
- **Model AI**: TinyLlama-1.1B, GPT-3.5 (fallback)
- **Database**: PostgreSQL (Supabase)
- **API**: Brave Search API, GPT API

## 📂 Struktur Repositori
```
/HalluGuard
├── /streamlit_app.py # Kode frontend (Streamlit)
├── /.streamlit/ # API Key
├── README.md # File README ini
└── requirements.txt # Dependensi Python
```

## 📊 Hasil dan Evaluasi
Klasifikasi Fakta dan Opini
HalluGuard berhasil membedakan antara fakta dan opini dengan akurasi yang tinggi. Berikut adalah contoh hasil klasifikasi:

