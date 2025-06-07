from aiogram.fsm.state import StatesGroup, State

class AddTask(StatesGroup):
    waiting_for_title = State()
    waiting_for_category = State()
    waiting_for_deadline = State()

class EditTask(StatesGroup):
    selecting_task = State()
    choosing_field = State()
    editing_field = State()
