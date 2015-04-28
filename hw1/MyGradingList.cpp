#include <boost/python.hpp>
#include <iostream>
#define private public
#include "MyList.h"
#undef private

using namespace boost::python;

typedef int (MyList::*char_find)(char&) const;
typedef int (MyList::*Mylist_find)(MyList&) const;

char_find find1= &MyList::find;
Mylist_find find2 = &MyList::find;

void assignMyList(MyList& self, const MyList& other)
{
    self = other;
}

std::string get_MyList(const MyList &l)
{
  std::string return_str;
  Node *head = l.head;

  if(head == NULL)
    return return_str;

	while(head->next != l.head)
	{
			return_str += head->value;
			head = head->next;
	}
  return_str += head->value;

  return return_str;
}

BOOST_PYTHON_MODULE(MyList)
{
  class_<MyList>("MyList")
      .def(init<std::string>())
      .def(init<const MyList::MyList>())
      .def("print_list", &MyList::print)
      .def("push_front", &MyList::push_front)
      .def("push_back", &MyList::push_back)
      .def("pop_back", &MyList::pop_back)
      .def("pop_front", &MyList::pop_front)
      .def("reverse", &MyList::reverse)
      .def("size", &MyList::size)
      .def("swap", &MyList::swap)
      .def("find_MyList", find1)
      .def("find_MyList", find2)
      .def("insert_at_pos", &MyList::insert_at_pos)
      .def(self + self)
      .def("reassign", assignMyList);
      ;
  def("get_MyList", get_MyList);
}
