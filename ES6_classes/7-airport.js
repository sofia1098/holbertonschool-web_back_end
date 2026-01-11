export default class Airport {
    constructr(name, code) {
      this._name = name;
      this._code = code;
      this[Symbol.toStringTag] = code;
    }
  }
