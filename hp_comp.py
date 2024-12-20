import timeit
from filters.fir_filter_highpass import highpass_fir_filter_opt_manual, highpass_fir_filter_firwin, plot_highpass_filter_opt_responses, plot_highpass_filter_opt_coefficients
from filters.fir_filter_highpass import highpass_fir_filter_manual, highpass_fir_filter_firwin, plot_highpass_filter_responses, plot_highpass_filter_coefficients

def measure_performance():
    """
    Measures the execution time of the original and optimized high-pass FIR filter design functions
    to evaluate the performance improvement.

    Parameters:
    None

    Returns:
    None

    The function prints:
    - The execution time of the original function.
    - The execution time of the optimized function.
    - The percentage improvement in performance.
    """

    cutoff_freq = 0.51  # Normalized cutoff frequency for the filter
    num_taps = 101  # Large number of taps for a more significant difference in measurement

    # Measure execution time of the original function
    original_time = timeit.timeit(
        stmt="highpass_fir_filter_manual(cutoff_freq, num_taps)",
        setup=(
            "from filters.fir_filter_highpass import highpass_fir_filter_manual;"
            "cutoff_freq = 0.51; num_taps = 101"
        ),
        number=10
    )

    # Measure execution time of the optimized function
    optimized_time = timeit.timeit(
        stmt="highpass_fir_filter_opt_manual(cutoff_freq, num_taps)",
        setup=(
            "from filters.fir_filter_highpass import highpass_fir_filter_opt_manual;"
            "cutoff_freq = 0.51; num_taps = 101"
        ),
        number=10
    )

    # Print the results
    print(f"Original function time: {original_time}")
    print(f"Optimized function time: {optimized_time}")
    improvement = ((original_time - optimized_time) / original_time) * 100
    print(f"Performance improvement: {improvement:.2f}%")

if __name__ == "__main__":
    measure_performance()
