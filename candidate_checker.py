#!/usr/bin/env python3
"""
Sprawdza podstawowy format zgłoszenia (nie jakość!)
Użycie: python candidate_checker.py ./moje_rozwiazanie/
"""

import pandas as pd
import json
import os
import sys

class CandidateChecker:
    def check_submission(self, submission_path):
        """Sprawdź podstawowe wymagania zgłoszenia"""
        print("🔍 PODSTAWOWY SPRAWDZACZ ZGŁOSZENIA")
        print("=" * 50)
        print("⚠️  To sprawdza tylko format i completeness!")
        print("    Faktyczna ocena będzie znacznie bardziej szczegółowa.\n")
        
        if not os.path.exists(submission_path):
            print(f"❌ Folder {submission_path} nie istnieje!")
            return False
        
        checks_passed = 0
        total_checks = 5

        print("📁 Sprawdzanie plików...")
        required_files = ['results.json', 'predictions.csv', 'solution_summary.md']
        files_ok = True
        
        for file in required_files:
            if os.path.exists(os.path.join(submission_path, file)):
                print(f"✅ {file} - znaleziono")
            else:
                print(f"❌ {file} - BRAKUJE!")
                files_ok = False
        
        if files_ok:
            checks_passed += 1

        print("\n📊 Sprawdzanie results.json...")
        results_path = os.path.join(submission_path, 'results.json')
        if os.path.exists(results_path):
            try:
                with open(results_path, 'r', encoding='utf-8') as f:
                    results = json.load(f)

                required_sections = ['candidate_info', 'data_analysis', 'model_performance', 'business_analysis']
                sections_ok = True
                
                for section in required_sections:
                    if section in results:
                        print(f"✅ Sekcja '{section}' - obecna")
                    else:
                        print(f"❌ Sekcja '{section}' - BRAKUJE!")
                        sections_ok = False
                
                if sections_ok:
                    checks_passed += 1

                if 'data_analysis' in results:
                    da = results['data_analysis']
                    required_metrics = [
                        'overall_ctr', 'position_bias_ratio', 'electronics_ctr', 
                        'quality_correlation', 'best_category'
                    ]
                    metrics_ok = True
                    
                    for metric in required_metrics:
                        if metric in da and da[metric] is not None:
                            print(f"✅ Metryka '{metric}' - obecna")
                        else:
                            print(f"❌ Metryka '{metric}' - BRAKUJE!")
                            metrics_ok = False
                    
                    if metrics_ok:
                        checks_passed += 1
                
            except Exception as e:
                print(f"❌ Błąd czytania results.json: {e}")

        print("\n📈 Sprawdzanie predictions.csv...")
        pred_path = os.path.join(submission_path, 'predictions.csv')
        if os.path.exists(pred_path):
            try:
                pred_df = pd.read_csv(pred_path)

                required_cols = ['session_id', 'product_id', 'actual_clicked', 'predicted_score']
                cols_ok = True
                
                for col in required_cols:
                    if col in pred_df.columns:
                        print(f"✅ Kolumna '{col}' - obecna")
                    else:
                        print(f"❌ Kolumna '{col}' - BRAKUJE!")
                        cols_ok = False
                
                if cols_ok:
                    checks_passed += 1

                    print(f"ℹ️  Rozmiar zbioru testowego: {len(pred_df)} wierszy")
                    print(f"ℹ️  Liczba sesji: {pred_df['session_id'].nunique()}")
                    
                    pred_min = pred_df['predicted_score'].min()
                    pred_max = pred_df['predicted_score'].max()
                    print(f"ℹ️  Zakres predicted_score: {pred_min:.3f} - {pred_max:.3f}")
                    
                    if pred_max > pred_min + 0.01:
                        print("✅ Model wydaje się dyskryminować")
                    else:
                        print("⚠️  Model może nie dyskryminować (wszystkie wyniki podobne)")
                
            except Exception as e:
                print(f"❌ Błąd czytania predictions.csv: {e}")

        print("\n🎯 Sprawdzanie modelu...")
        try:
            if 'model_performance' in results:
                mp = results['model_performance']
                ndcg = float(mp.get('ndcg_at_5', 0))
                features_count = int(mp.get('features_count', 0))
                
                if 0.3 <= ndcg <= 1.0:
                    print(f"✅ NDCG@5 w rozsądnym zakresie: {ndcg}")
                    checks_passed += 1
                else:
                    print(f"⚠️  NDCG@5 może być błędne: {ndcg} (oczekiwane 0.3-1.0)")
                
                if features_count >= 5:
                    print(f"✅ Liczba features OK: {features_count}")
                else:
                    print(f"⚠️  Za mało features: {features_count} (wymagane ≥5)")
                    
        except Exception as e:
            print(f"⚠️  Nie można sprawdzić metryki modelu: {e}")

        print(f"\n📊 PODSUMOWANIE:")
        print(f"Zaliczone sprawdzenia: {checks_passed}/{total_checks}")
        
        if checks_passed >= 4:
            print("✅ GOTOWE DO WYSŁANIA!")
            print("   Format wygląda dobrze. Możesz wysłać zgłoszenie.")
            return True
        elif checks_passed >= 2:
            print("⚠️  WYMAGA POPRAWEK")
            print("   Część wymagań nie spełniona. Popraw przed wysłaniem.")
            return False
        else:
            print("❌ NIE GOTOWE")
            print("   Większość wymagań nie spełniona. Sprawdź instrukcje.")
            return False

def main():
    """Główna funkcja checkera"""
    
    if len(sys.argv) != 2:
        print("🎯 ML ENGINEER CHALLENGE - CANDIDATE CHECKER")
        print("=" * 50)
        print("Sprawdza podstawowy format zgłoszenia (nie jakość analizy!)\\n")
        print("Użycie: python candidate_checker.py <folder_zgloszczenia>")
        print("\\nPrzykład:")
        print("  python candidate_checker.py ./moje_rozwiazanie/")
        sys.exit(1)
    
    submission_path = sys.argv[1]
    
    checker = CandidateChecker()
    success = checker.check_submission(submission_path)
    
    print("\\n" + "="*50)
    if success:
        print("🎉 Format zgłoszenia wygląda dobrze!")
        print("💡 Pamiętaj: to tylko sprawdzenie formatu.")
        print("   Jakość analizy będzie oceniana osobno przez zespół.")
    else:
        print("🔧 Zgłoszenie wymaga poprawek przed wysłaniem.")

if __name__ == "__main__":
    main()