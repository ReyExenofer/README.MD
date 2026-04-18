// src/features/interaction/interactionSlice.js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  hcp_name: "",
  date: "",
  time: "",
  attendees: [],
  topics: [],
  summary: "",
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    updateInteraction(state, action) {
      return { ...state, ...action.payload };
    },
  },
});

export const { updateInteraction } = interactionSlice.actions;
export default interactionSlice.reducer;
