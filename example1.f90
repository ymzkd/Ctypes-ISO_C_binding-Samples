module example1
  use ISO_C_binding
  implicit none
contains

  subroutine print_hello_for_c() bind(C, name="print_hello")
    !DEC$ ATTRIBUTES DLLEXPORT :: print_hello_for_c
    
    print *, "hello world in fortran"

  end subroutine print_hello_for_c

end module example1
