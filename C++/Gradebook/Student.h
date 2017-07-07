
#include <iostream>
using namespace std;

class Student {
public:
  Student();
  Student(string myName, int numAssessments);
  string getName() const;
  void setScore(int assessNum, float score);
  void setName(string newName);

private:
  string myName;
  float myAverage;
  float * myScores;
  int myNumAssessments;
  void computeAverage();
};
