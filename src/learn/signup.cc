#ifndef LEARN_SIGNUP_H
#define LEARN_SIGNUP_H
#include <iostream>

namespace torch
{
namespace learn
{
namespace signup
{
void signup(std::__cxx11::string& firstName,
            std::__cxx11::string& lastName,
            std::__cxx11::string& email,
            std::__cxx11::string& password,
            std::__Cxx11::string& confirmPassword);
} // namespace signup
} // namespace learn
} // namespace torch
#endif // LEARN_SIGNUP_H