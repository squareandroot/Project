debug:
	g++ performance_RK_vs_LMM.cpp -o performance_RK_vs_LMM -Wall -D_GLIBCXX_DEBUG -g
release:
	g++ performance_RK_vs_LMM.cpp -o performance_RK_vs_LMM -Wall -O3
