	private static {{Name}}Factory 		{{name}}Factory 			= null;

	public static {{Name}}Factory get{{Name}}Factory() {
		if ({{name}}Factory == null)
			{{name}}Factory = new {{Name}}Factory();
		return {{name}}Factory;
	}
