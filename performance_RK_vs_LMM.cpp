#include <stdlib.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <fstream>
#include <sstream>

using namespace std;

vector<double> linspace(double start, double end, int num)
{
    vector<double> linspaced;

    if (num == 0)
    {
        return linspaced;
    }
    if (num == 1)
    {
        linspaced.push_back(start);
        return linspaced;
    }

    double delta = (end - start) / (num - 1);

    for (int i = 0; i < num - 1; i++)
    {
        linspaced.push_back(start + delta * i);
    }
    linspaced.push_back(end);

    return linspaced;
}

vector<double> RK4(const double &t0, const double &tn, const int &n, const double &y0, double (*func)(double, double), double &exec_time)
{
    double h = (tn - t0) / n;
    vector<double> t = linspace(t0, tn, n + 1);
    vector<double> y(n + 1);
    y[0] = y0;

    auto t1 = chrono::high_resolution_clock::now();

    for (int i = 0; i < n; i++)
    {
        double K1 = func(t[i], y[i]);
        double K2 = func(t[i] + h / 2, y[i] + K1 * h / 2);
        double K3 = func(t[i] + h / 2, y[i] + K2 * h / 2);
        double K4 = func(t[i] + h, y[i] + K3 * h);
        y[i + 1] = y[i] + h * (K1 + 2 * K2 + 2 * K3 + K4) / 6;
    }

    auto t2 = chrono::high_resolution_clock::now();

    exec_time = chrono::duration_cast<chrono::nanoseconds>(t2 - t1).count();
    return y;
}

vector<double> AdamsBashforth4(const double &t0, const double &tn, const int &n, const double &y0, double (*func)(double, double), double &exec_time)
{
    double h = (tn - t0) / n;
    vector<double> t = linspace(t0, tn, n + 1);
    vector<double> y(n + 1);
    vector<double> y_start = RK4(t0, t0 + 3 * h, 3, y0, *func, exec_time);

    y[0] = y_start[0];
    y[1] = y_start[1];
    y[2] = y_start[2];
    y[3] = y_start[3];

    auto t1 = chrono::high_resolution_clock::now();

    double K1 = func(t[2], y[2]);
    double K2 = func(t[1], y[1]);
    double K3 = func(t[0], y[0]);
    double K4;
    for (int i = 3; i < n; i++)
    {
        K4 = K3;
        K3 = K2;
        K2 = K1;
        K1 = func(t[i], y[i]);
        y[i + 1] = y[i] + h / 24 * (55 * K1 - 59 * K2 + 37 * K3 - 9 * K4);
    }

    auto t2 = chrono::high_resolution_clock::now();

    exec_time = chrono::duration_cast<chrono::nanoseconds>(t2 - t1).count();
    return y;
}

vector<double> AdamsBashforth5(const double &t0, const double &tn, const int &n, const double &y0, double (*func)(double, double), double &exec_time)
{
    double h = (tn - t0) / n;
    vector<double> t = linspace(t0, tn, n + 1);
    vector<double> y(n + 1);
    vector<double> y_start = RK4(t0, t0 + 4 * h, 4, y0, *func, exec_time);

    y[0] = y_start[0];
    y[1] = y_start[1];
    y[2] = y_start[2];
    y[3] = y_start[3];
    y[4] = y_start[4];

    auto t1 = chrono::high_resolution_clock::now();

    double K1 = func(t[3], y[3]);
    double K2 = func(t[2], y[2]);
    double K3 = func(t[1], y[1]);
    double K4 = func(t[0], y[0]);
    double K5;
    for (int i = 4; i < n; i++)
    {
        K5 = K4;
        K4 = K3;
        K3 = K2;
        K2 = K1;
        K1 = func(t[i], y[i]);
        y[i + 1] = y[i] + h / 720 * (1901 * K1 - 2774 * K2 + 2616 * K3 - 1274 * K4 + 251 * K5);
    }

    auto t2 = chrono::high_resolution_clock::now();

    exec_time = chrono::duration_cast<chrono::nanoseconds>(t2 - t1).count();
    return y;
}

double f(double t, double y)
{
    return y;
}

int main(int argc, char *argv[])
{
    double exec_time;
    double start = atof(argv[1]);
    double end = atof(argv[2]);
    double n = atof(argv[3]);

    string arg1(argv[1]);
    string arg2(argv[2]);
    string arg3(argv[3]);

    string filename_RK4 = "./out/RK4-" + arg3 + ".dat";
    string filename_AB4 = "./out/AB4-" + arg3 + ".dat";
    string filename_AB5 = "./out/AB5-" + arg3 + ".dat";

    vector<double> solution_RK4 = RK4(start, end, n, 1, *f, exec_time);
    int n_RK4 = solution_RK4.size();
    ofstream fs1(filename_RK4);
    fs1.precision(15);
    fs1 << exec_time << " ns" << endl;
    for (int i = 0; i < n_RK4; i++)
    {
        fs1 << solution_RK4[i] << endl;
    }
    fs1.close();

    vector<double> solution_AB4 = AdamsBashforth4(start, end, n, 1, *f, exec_time);
    int n_AB4 = solution_AB4.size();
    ofstream fs2(filename_AB4);
    fs2.precision(15);
    fs2 << exec_time << " ns" << endl;
    for (int i = 0; i < n_AB4; i++)
    {
        fs2 << solution_AB4[i] << endl;
    }
    fs2.close();

    vector<double> solution_AB5 = AdamsBashforth5(start, end, n, 1, *f, exec_time);
    int n_AB5 = solution_AB5.size();
    ofstream fs3(filename_AB5);
    fs3.precision(15);
    fs3 << exec_time << " ns" << endl;
    for (int i = 0; i < n_AB5; i++)
    {
        fs3 << solution_AB5[i] << endl;
    }
    fs3.close();
}
