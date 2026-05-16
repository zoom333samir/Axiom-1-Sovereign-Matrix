import time
import numpy as np

class Axiom1Matrix:
    """
    AXIOM-1 Sovereign Matrix Simulation
    A 6-stage filtering architecture for governing AI output reliability.
    """

    def __init__(self, stability_threshold=0.85, resonance_freq=12.8):
        self.stability_threshold = stability_threshold
        self.resonance_freq = resonance_freq
        print("="*60)
        print("[System] Initializing AXIOM-1 Sovereign Matrix...")
        print(f"[Config] Stability Threshold: {self.stability_threshold}")
        print(f"[Config] Resonance Frequency: {self.resonance_freq} Hz")
        print("="*60)
        time.sleep(1)

    # Stage 1: Lexical Coherence
    def _stage1_lexical_coherence(self, text):
        return len(text.split()) > 3

    # Stage 2: Spectral Stability (Eigenvalue analysis)
    def _stage2_spectral_stability(self, text):
        matrix = np.array([[0.8, 0.2],
                           [0.1, 0.9]])
        eigenvalues, _ = np.linalg.eig(matrix)
        stability_index = max(abs(eigenvalues))
        if any(word in text.lower() for word in ["logic","framework","design"]):
            stability_index += 0.05
        return stability_index >= self.stability_threshold, stability_index

    # Stage 3: Logical Consistency
    def _stage3_logical_consistency(self, text):
        contradictions = ["always true but false","certainly uncertain","true and false"]
        return not any(c in text.lower() for c in contradictions)

    # Stage 4: Burden Evaluation
    def _stage4_burden_evaluation(self, text):
        high_burden_keywords = ["must","absolute","always","never","100%"]
        burden_score = sum(text.lower().count(k) for k in high_burden_keywords)
        return burden_score > 0, burden_score

    # Stage 5: Pulse Operator (12.8 Hz correction)
    def _stage5_pulse_operator(self, stability_index):
        if stability_index < self.stability_threshold:
            adjusted_index = stability_index + (self.resonance_freq/100)  # 12.8Hz effect
            return adjusted_index >= self.stability_threshold, adjusted_index
        return True, stability_index

    # Stage 6: Governed Release Decision
    def _stage6_governed_release(self, metrics):
        if not metrics['stage1'] or not metrics['stage3']:
            return "REJECTED", 0.0
        if metrics['stage2_val'] < self.stability_threshold:
            if metrics['high_burden']:
                return "REJECTED", metrics['stage2_val']
            else:
                return "QUALIFIED", metrics['stage2_val']
        return "ACCEPTED", metrics['stage2_val']

    # Evaluation pipeline
    def evaluate_output(self, llm_output):
        print(f"\n[Candidate Output]: '{llm_output[:60]}...'")
        print("-"*40)
        metrics = {}
        metrics['stage1'] = self._stage1_lexical_coherence(llm_output)
        metrics['stage2_pass'], metrics['stage2_val'] = self._stage2_spectral_stability(llm_output)
        metrics['stage3'] = self._stage3_logical_consistency(llm_output)
        metrics['high_burden'], metrics['burden_score'] = self._stage4_burden_evaluation(llm_output)
        metrics['pulse_pass'], metrics['pulse_val'] = self._stage5_pulse_operator(metrics['stage2_val'])
        decision, confidence = self._stage6_governed_release(metrics)

        print(f"[*] Stage 1 (Lexical):        {'PASS' if metrics['stage1'] else 'FAIL'}")
        print(f"[*] Stage 2 (Spectral Index): {metrics['stage2_val']:.2f} / 1.00")
        print(f"[*] Stage 3 (Consistency):    {'PASS' if metrics['stage3'] else 'FAIL'}")
        print(f"[*] Stage 4 (Burden Score):   {metrics['burden_score']} ({'HIGH' if metrics['high_burden'] else 'STANDARD'})")
        print(f"[*] Stage 5 (Pulse Operator): {'PASS' if metrics['pulse_pass'] else 'FAIL'}")
        print(f"\n[>>>] FINAL A1M DECISION: {decision} (Confidence: {confidence:.2f})")
        print("="*60)
        return decision

# ==========================================
# SIMULATION EXECUTION
# ==========================================
if __name__ == "__main__":
    matrix = Axiom1Matrix(stability_threshold=0.80)

    # Test Case 1: Coherent logical output
    matrix.evaluate_output("The framework utilizes a sovereign logic to ensure stability.")

    time.sleep(1.5)

    # Test Case 2: Contradictory high-burden output
    matrix.evaluate_output("This is an absolute fact, it is always true but false in every case.")

    time.sleep(1.5)

    # Test Case 3: Short/random output
    matrix.evaluate_output("abc xyz")
