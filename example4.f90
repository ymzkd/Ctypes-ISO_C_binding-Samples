module example4
  use ISO_C_binding
  implicit none

contains

  subroutine sum_all_sub(arr_length, array, result) bind(C, name="sum_all_sub")
    !DEC$ ATTRIBUTES DLLEXPORT :: sum_all_sub
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    integer(c_int), intent(out) :: result

    result = sum(array(:))

  end subroutine sum_all_sub

  function sum_all_func(arr_length, array) bind(C, name="sum_all_func")
    !DEC$ ATTRIBUTES DLLEXPORT :: sum_all_func
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    integer(c_int) :: sum_all_func

    sum_all_func = sum(array(:))

  end function sum_all_func

  subroutine shift_all_sub(offset, arr_length, array, result_array) bind(C, name="shift_all_sub")
    !DEC$ ATTRIBUTES DLLEXPORT :: shift_all_sub
    integer(c_int), intent(in) :: offset
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    integer(c_int), intent(out) :: result_array(arr_length)

    result_array(:) = array(:) + offset

  end subroutine shift_all_sub

  function shift_all_func(offset, arr_length, array) bind(C, name="shift_all_func")
    !DEC$ ATTRIBUTES DLLEXPORT :: shift_all_func
    integer(c_int), intent(in) :: offset
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    type(C_ptr) :: shift_all_func
    integer(c_int), pointer :: work_array(:)

    ! 動的割付
    allocate(work_array(arr_length))
    work_array(:) = array(:) + offset

    ! Cポインタを作成
    shift_all_func = C_loc(work_array)

  end function shift_all_func

  subroutine delete_array(arr_length, array) bind(C, name="delete_array")
    !DEC$ ATTRIBUTES DLLEXPORT :: delete_array
    integer(c_int), intent(in) :: arr_length
    type(c_ptr), value :: array
    integer(c_int), pointer :: work_array(:)

    call C_F_pointer(array, work_array, [arr_length])
    deallocate(work_array)

    ! C_NULL_PTR定数を利用してCポインタをnullにする。
    array = C_NULL_PTR

  end subroutine delete_array

end module example4
