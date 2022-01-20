#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <fstream>

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

vector<double> RK4(const double &t0, const double &tn, const int &n, const double &y0, double (*func)(double, double))
{
    double h = (tn - t0) / n;
    vector<double> t = linspace(t0, tn, n + 1);
    vector<double> y(n + 1);
    y[0] = y0;

    for (int i = 0; i < n; i++)
    {
        double K1 = func(t[i], y[i]);
        double K2 = func(t[i] + h / 2, y[i] + K1 * h / 2);
        double K3 = func(t[i] + h / 2, y[i] + K2 * h / 2);
        double K4 = func(t[i] + h, y[i] + K3 * h);
        y[i + 1] = y[i] + h * (K1 + 2 * K2 + 2 * K3 + K4) / 6;
    }

    return y;
}

vector<double> AdamsBashforth4(const double &t0, const double &tn, const int &n, const double &y0, double (*func)(double, double))
{
    double h = (tn - t0) / n;
    vector<double> t = linspace(t0, tn, n + 1);
    vector<double> y(n + 1);
    vector<double> y_start = RK4(t0, t0 + 3 * h, 3, y0, *func);
    y[0] = y_start[0];
    y[1] = y_start[1];
    y[2] = y_start[2];
    y[3] = y_start[3];
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
    return y;
}

double f(double t, double y)
{
    return y;
}

int main()
{
    vector<double> solution_RK4 = RK4(0.0, 1.0, 100, 1, *f);
    vector<double> solution_AB4 = AdamsBashforth4(0.0, 1.0, 100, 1, *f);
    int n_RK4 = solution_RK4.size();
    int n_AB4 = solution_AB4.size();
    ofstream fs("out.dat");
    fs.precision(15);
    fs << "RK4" << endl;
    for (int i = 0; i < n_RK4; i++)
    {
        fs << solution_RK4[i] << endl;
    }
    fs << "AB4" << endl;
    for (int i = 0; i < n_AB4; i++)
    {
        fs << solution_AB4[i] << endl;
    }
    fs.close();
}
