module example5
  use ISO_C_binding
  implicit none
  type, bind(C) :: report
    integer(c_int) :: len
  end type report

  integer, pointer :: extruct_array(:)

contains

  function extruct_plus(arr_length, array) bind(C, name="extruct_plus")
    !DEC$ ATTRIBUTES DLLEXPORT :: extruct_plus
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    type(report) :: extruct_plus
    integer(c_int) :: plus_count

    plus_count = count(array(:)>=0)
    ! 動的割付
    allocate(extruct_array(plus_count))
    extruct_array(:) = pack(array(:), mask=(array(:)>=0))

    extruct_plus%len = plus_count

  end function extruct_plus

  subroutine get_array(arr_length, array) bind(C, name="get_array")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_array
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(inout) :: array(arr_length)

    array(:) = extruct_array(:)

  end subroutine get_array

  subroutine delete_array() bind(C, name="delete_array")
    !DEC$ ATTRIBUTES DLLEXPORT :: delete_array

    ! 割り付けたモジュール変数を解放
    deallocate(extruct_array)

  end subroutine delete_array

end module example5
