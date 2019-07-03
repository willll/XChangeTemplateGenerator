package exchanges;

import org.knowm.xchange.ExchangeFactory;
import org.knowm.xchange.{{name}}.{{Name}}Exchange;

public class {{Name}} extends GenericExchange {
	public {{Name}}() {
		this.exchange = ExchangeFactory.INSTANCE.createExchange({{Name}}Exchange.class.getName());
	}
}