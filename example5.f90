module example5
  use ISO_C_binding
  implicit none
  type, bind(C) :: result
    integer(c_int) :: len
    type(c_ptr) :: arr
  end type result

contains

  function extruct_plus(arr_length, array) bind(C, name="extruct_plus")
    !DEC$ ATTRIBUTES DLLEXPORT :: extruct_plus
    integer(c_int), intent(in) :: arr_length
    integer(c_int), intent(in) :: array(arr_length)
    type(result) :: extruct_plus
    integer(c_int) :: plus_count
    integer(c_int), pointer :: work_array(:)

    plus_count = count(array(:)>=0)
    allocate(work_array(plus_count))
    work_array(:) = pack(array(:), mask=(array(:)>=0))

    extruct_plus%len = plus_count
    extruct_plus%arr = C_loc(work_array)

  end function extruct_plus

  subroutine delete_array(arr_length, array) bind(C, name="delete_array")
    !DEC$ ATTRIBUTES DLLEXPORT :: delete_array
    integer(c_int), intent(in) :: arr_length
    type(c_ptr), value :: array
    integer(c_int), pointer :: work_array(:)

    call C_F_pointer(array, work_array, [arr_length])
    deallocate(work_array)

    ! ISO_C_bindingではC_NULL_PTRにC_ptr型のnullが定数として格納されている。
    array = C_NULL_PTR

  end subroutine delete_array

end module example5
