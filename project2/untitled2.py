# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:46:34 2018

@author: Charlotte
"""

#include <iostream>
#include <vector>
#include <cfloat>
#include <iomanip>
using std::vector;
using std::cin;
using std::cout;
using std::string;
int main (int argc, char *argv[]) {
	int m = 0, n = 0;
	cin >> n >> m;

	double result = 0, orignalPriceSum = 0;
	while(n > 0) {
		int originalPrice = 0, discountable = -1;
		cin >> originalPrice >> discountable;
		orignalPriceSum += originalPrice;
		if(discountable == 1) {
			result += originalPrice * 0.8;
		} else {
			result += originalPrice;
		}
		n--;
	}
	double resultUsePreferential = DBL_MAX;
	while(m > 0) {
		m--;
		int limit = 0, subtract = 0;
		cin >> limit >> subtract;
		if(orignalPriceSum >= limit) {
			resultUsePreferential = std::min(orignalPriceSum - subtract, resultUsePreferential);
		}
	}
	result = std::min(result , resultUsePreferential);
	cout << std::setprecision(2) << std::setiosflags(std::ios::fixed) << result;
	return 0;
}