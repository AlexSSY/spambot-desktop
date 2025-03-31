<template>
  <div class="w-full p-4 bg-slate-100 shadow-md rounded-lg">
    <div class="relative">
      <textarea
        id="message"
        class="w-full max-h-40 overflow-hidden resize-none p-3 text-sm border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
        placeholder="Write a message..."
        rows="1"
        @input=""
      >
      </textarea>

      <!-- Send Button -->
      <button
        class="absolute bottom-[3px] right-2 text-blue-500 rounded-full p-2 hover:text-blue-600 transition-all"
      >
        <font-awesome-icon :icon="['fab', 'telegram']" class="text-xl" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    adjustHeight(event) {
      const el = event.target;
      el.style.height = "auto"; // Reset height
      el.style.height = el.scrollHeight + "px"; // Set new height
    },
  },
};
</script>
