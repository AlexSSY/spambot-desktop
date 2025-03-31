<template>
  <button :class="buttonClass">{{ text }}</button>
</template>

<script>
export default {
  name: "button",
  props: {
    variant: {
      type: String,
      default: "primary",
    },
    size: {
      type: String,
      default: "base",
    },
    text: {
      type: String,
      required: true,
    },
  },
  computed: {
    buttonClass() {
      var base = "rounded-lg shadow-md transition";

      var sizes = {
        base: "px-3 py-2 text-sm",
        big: "px-6 py-3"
      };

      var variants = {
        primary: "text-white bg-indigo-600 shadow-indigo-400 hover:bg-indigo-700",
        secondary: "text-gray-900 bg-gray-300 shadow-gray-400 hover:bg-gray-400",
        success: "text-white bg-green-600 shadow-green-400 hover:bg-green-700",
        danger: "text-white bg-red-600 shadow-red-400 hover:bg-red-700",
      };

      return `${base} ${sizes[this.size]} ${variants[this.variant] || variants.primary}`;
    },
  },
};
</script>
