#include <boost/python.hpp>
#include <iostream>
#include "MyList.hpp"

using namespace boost::python;

int (MyList::*find1)(char) const = &MyList::find;
int (MyList::*find2)(MyList::MyList&) const = &MyList::find;

void assignMyList(MyList& self, const MyList& other)
{
    self = other;
}
BOOST_PYTHON_MODULE(MyList)
{
  class_<MyList>("MyList", init<std::string>())
      .def(init<MyList::MyList>())
      .def("print_list", &MyList::print)
      .def("__getitem__", &MyList::operator[])
      .def("push_front", &MyList::push_front)
      .def("push_back", &MyList::push_back)
      .def("pop_back", &MyList::pop_back)
      .def("pop_front", &MyList::pop_front)
      .def("reverse", &MyList::reverse)
      .def("size", &MyList::size)
      .def("swap", &MyList::swap)
      .def("find", find1)
      .def("find", find2)
      .def("insert_at_pos", &MyList::insert_at_pos)
      .def(self + self)
      .def("reassign", assignMyList);
      ;
}
