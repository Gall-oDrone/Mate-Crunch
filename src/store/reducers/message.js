import { 
  ADD_MESSAGE,
  SET_MESSAGES,
  SET_STATUS,
  GET_CHATS_SUCCESS
} from "../actions/actionTypes";

import { updateObject } from "../utility";

const initialState = {
  messages: [],
  chats: [],
  status: null
};

const addMessage = (state, action) => {
  return updateObject(state, {
    messages: [...state.messages, action.message]
  });
};

const setMessages = (state, action) => {
  console.log("OH T OH T: ", action.messages.reverse())
  return updateObject(state, {
    messages: action.messages
  });
};

const setStatus = (state, action) => {
  return updateObject(state, {
    status: action.status
  });
}

const setChats = (state, action) => {
  return updateObject(state, {
    chats: action.chats
  });
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_MESSAGE:
      return addMessage(state, action);
    case SET_MESSAGES:
      return setMessages(state, action);
    case SET_STATUS:
      return setStatus(state, action);
    case GET_CHATS_SUCCESS:
      return setChats(state, action);
    default:
      return state;
  }
};

export default reducer;