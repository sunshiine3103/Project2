from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from states.task import AddTask

router = Router()

@router.message(Command("add"))
async def add_task_start(message: Message, state: FSMContext):
    await state.set_state(AddTask.waiting_for_title)
    await message.answer("Введите название задачи:")

@router.message(AddTask.waiting_for_title)
async def add_task_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddTask.waiting_for_category)
    await message.answer("Выберите категорию:", reply_markup=category_keyboard())
