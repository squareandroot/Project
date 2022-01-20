debug:
	g++ performance_RK_vs_LMM.cpp -o performance_RK_vs_LMM.out -Wall -D_GLIBCXX_DEBUG -g && ./performance_RK_vs_LMM.out
release:
	g++ performance_RK_vs_LMM.cpp -o performance_RK_vs_LMM.out -Wall -O3 && ./performance_RK_vs_LMM.out
