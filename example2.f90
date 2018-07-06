module example2
  use ISO_C_binding
  implicit none

  ! スカラー
  integer(C_int) :: int_val

  ! 配列
  integer(C_int), parameter :: array_length = 10
  integer(C_int) :: array(array_length)

  ! 構造体
  type, bind(C) :: day
    integer(C_int) :: month
    integer(C_int) :: day
  end type day

contains

  function add(val_a, val_b) bind(C, name="add")
    !DEC$ ATTRIBUTES DLLEXPORT :: add
    integer(c_int), intent(in) :: val_a, val_b
    integer(c_int) :: add

    add = val_a + val_b

  end function add

end module example2
