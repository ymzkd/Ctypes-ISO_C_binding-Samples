module example3
  use ISO_C_binding
  implicit none

  ! 構造体
  type, bind(C) :: day_type
    integer(c_int) :: month
    integer(c_int) :: date
  end type day_type

contains

  subroutine input(val_int, arr_length, val_arr, val_type) bind(C, name="input")
    !DEC$ ATTRIBUTES DLLEXPORT :: input
    integer(c_int), intent(in) :: val_int
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: val_arr(arr_length)
    type(day_type), intent(in) :: val_type

    print *, "scaler variable :", val_int
    print *, "array variable :", val_arr(:)
    print *, "type variable : month ", val_type%month, " date ", val_type%date

  end subroutine input

end module example3
