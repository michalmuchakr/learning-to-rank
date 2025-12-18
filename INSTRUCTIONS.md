
🎯 ZADANIE ML ENGINEER - LEARNING-TO-RANK

🔧 JĘZYK: Dowolny (Python, R, Scala, ..)
📊 CEL: Zbuduj model rankujący produkty w wyszukiwarce e-commerce

═══════════════════════════════════════════════════════════════════════════════

📁 DOSTARCZONE PLIKI:
├── search_sessions.csv         # Dataset do analizy
├── candidate_checker.py           # Sprawdzacz formatu (dla Ciebie)
├── expected_format.json       # Wzór formatu odpowiedzi
└── INSTRUCTIONS.md            # Te instrukcje

📁 TWOJE PLIKI DO DOSTARCZENIA:
├── results.json               # Wyniki analizy (DOKŁADNY format!)
├── predictions.csv            # Predykcje modelu na zbiorze testowym
├── solution_summary.md        # Krótkie podsumowanie (2-3 akapity)
└── solution.[py/R/scala/...]  # Twój kod (opcjonalnie)

═══════════════════════════════════════════════════════════════════════════════

📊 DATASET: search_sessions.csv
- session_id: ID sesji wyszukiwania
- product_id: ID produktu
- position: pozycja na stronie (1-10)
- clicked: czy kliknięto (1=tak, 0=nie)
- price_pln: cena w PLN
- category: kategoria (Elektronika, Ksiazki, Odziez)
- quality_score: jakość produktu (0.0-1.0)
- user_preferred_category: preferowana kategoria użytkownika

═══════════════════════════════════════════════════════════════════════════════

🔍 CZĘŚĆ 1: ANALIZA DANYCH
Oblicz te 5 kluczowych metryk:

{
  "data_analysis": {
    "overall_ctr": 0.XXXX,                    # Wszystkie kliki / wszystkie wyświetlenia
    "position_bias_ratio": X.XX,              # CTR pozycja 1 / CTR pozycja 5  
    "electronics_ctr": 0.XXXX,                # CTR dla kategorii Elektronika
    "quality_correlation": 0.XXXX,            # Korelacja quality_score vs clicked
    "best_category": "NazwaKategorii"         # Kategoria z najwyższym CTR
  }
}

🤖 CZĘŚĆ 2: MODEL LEARNING-TO-RANK
Wymagania:

CECHY (minimum 5):
1. position_boost = 1/position
2. log_price = log(price_pln + 1)
3. quality_price_ratio = quality_score / log_price
4. category_match = (category == user_preferred_category) ? 1 : 0
5. [Twoja cecha]: Wymyśl dodatkową

METODOLOGIA:
□ Podziel dane po session_id (80% train, 20% test)
□ Użyj LightGBM/XGBoost/innego rankera
□ Osiągnij NDCG@5 > 0.50 na zbiorze testowym

WYNIKI:
{
  "model_performance": {
    "algorithm_used": "nazwa_algorytmu",
    "ndcg_at_5": 0.XXXX,                     # NDCG@5 na test set
    "features_count": X,                      # Liczba użytych cech
    "top_features": ["feat1", "feat2"]       # 2 najważniejsze cechy
  }
}

📈 CZĘŚĆ 3: BUSINESS SUMMARY
Krótka analiza biznesowa:

{
  "business_analysis": {
    "expected_ctr_lift_percent": XX,          # Oczekiwany wzrost CTR
    "main_risk": "krótki_opis",              # Główne ryzyko wdrożenia
    "recommendation": "deploy/test/reject"    # Twoja rekomendacja
  }
}

═══════════════════════════════════════════════════════════════════════════════

📄 KOMPLETNY FORMAT results.json:
{
  "candidate_info": {
    "language_used": "Python",
    "time_spent_hours": 1.3
  },
  "data_analysis": {
    "overall_ctr": 0.XXXX,
    "position_bias_ratio": X.XX,
    "electronics_ctr": 0.XXXX,
    "quality_correlation": 0.XXXX,
    "best_category": "Elektronika"
  },
  "model_performance": {
    "algorithm_used": "LightGBM",
    "ndcg_at_5": 0.XXXX,
    "features_count": 6,
    "top_features": ["position_boost", "quality_price_ratio"]
  },
  "business_analysis": {
    "expected_ctr_lift_percent": 15,
    "main_risk": "Position bias amplification",
    "recommendation": "deploy"
  }
}

📄 FORMAT predictions.csv:
session_id,product_id,actual_clicked,predicted_score
1,prod_1_1,1,0.85
1,prod_1_2,0,0.23
...
