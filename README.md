# chi_square_test_complex_survey_data
chi square test on complex survey data and normal chi square test

Code consitst of test of indepandence recommende to use on complex survey data.
Libralies needed PANDAS, numpy, scipy.
You can compare results of the tests with:


# EXAMPLE

prva_txt="name_of_variable"
druha_txt="name_of_variable"

#odstranenie nan hodnot
data = data[np.isfinite(data[prva_txt])]
data = data[np.isfinite(data[druha_txt])]

prva=data[prva_txt]
druha=data[druha_txt]

s=independance_test(prva, druha)
print s
v=independance_test_complex(prva,druha,prva_txt,druha_txt)
print v

